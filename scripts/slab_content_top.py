#!/usr/bin/env python

from __future__ import print_function

import re
import shlex
import sys
import subprocess

from collections import Counter

# suggested by WWG
# def direct_ptov(p_addr):
#   if p_addr >= phys_base:
#     return p_addr - phys_base + __START_KERNEL_map
#   else:
#     return p_addr + PAGE_OFFSET

def crash_cmd(crash_process, cmd):
    crash_process.stdin.write("%s\neval 1\n" % cmd)
    crash_process.stdin.flush()

    output = []
    while True:
        line = crash_process.stdout.readline()
        if line.endswith("%s\n" % '{:064}'.format(1)):
            break
        else:
            output.append(line.rstrip())

    return output[:-3]


def get_slab_addr_objsize(crash_process, slab_name):
    output = crash_cmd(crash_process, "kmem -s %s" % slab_name)
    for line in output:
        if line.startswith("CACHE"):
            objsize_index = line.split().index("OBJSIZE")
        elif line.startswith("ffff"):
            fields = line.split()
            addr = fields[0]
            objsize = int(fields[objsize_index])
            return addr, objsize
    else:
        print("Failed to parse slab objsize", file=sys.stderr)
        sys.exit(-1)


def page_address(page, vmemmap_base, page_offset_base):
    return (((page - vmemmap_base)/64) << 12) + page_offset_base


def get_bases(crash_process):
    vmemmap_base = 0xffffea0000000000
    page_offset_base = 0xffff880000000000

    output = crash_cmd(crash_process, "p -x vmemmap_base")
    addr = output[0].split()[-1]
    if addr.startswith("0xffff"):
        vmemmap_base = long(addr, base=16)

        output = crash_cmd(crash_process, "p -x page_offset_base")
        addr = output[0].split()[-1]
        page_offset_base = long(addr, base=16)

    return vmemmap_base, page_offset_base


def get_release(crash_process):
    cmd = "sys |grep RELEASE: | awk '{print $NF}'"
    output = crash_cmd(crash_process, cmd)
    return output[0]


def use_slub(crash_process):
    if get_release(crash_process).startswith("2"):
        return False
    return True


def get_content(crash_process, slab_name):
    vmemmap_base, page_offset_base = get_bases(crash_process)
    slab_addr, objsize = get_slab_addr_objsize(crash_process, slab_name)

    page_member = "slab_cache" if use_slub(crash_process) else "lru.next"
    cmd = "kmem -m %s | grep %s | awk '{print $1}'" % (page_member, slab_addr)
    output = crash_cmd(crash_process, cmd)

    rd_cmds = []
    for line in output:
        if line.startswith('ffff'):
            addr = page_address(long(line, base=16),
                                vmemmap_base, page_offset_base)
            rd_cmds.append("rd -x %x %d" % (addr, objsize/8))

    rd_cmds_output = []
    off = 0
    length = 1000
    while off < len(rd_cmds):
        cmd = "\n".join(rd_cmds[off:off+length])
        output = crash_cmd(crash_process, cmd)
        off += length
        # # Only return contents that startswith ffff
        # rd_cmds_output += [line for line in output if line.startswith('ffff')]
        rd_cmds_output += output

    return rd_cmds_output


def show(crash_process, top):
    print('Content          Count\tSymbol/Slab')
    for v, c in top:
        address = long(v, base=16)
        symbol = ""

        if 0xffff880000000000 < address < 0xffffc7ffffffffff:
            output = crash_cmd(crash_process, "kmem %s" % v)
            if output and output[0].startswith("CACHE"):
                name_idx = output[0].split().index("NAME")
                symbol += output[1].split()[name_idx]
        elif 0xffffffff80000000 < address < 0xfffffffffeffffff:
            cmd = "kmem %s |grep ^ffffffff | awk '{print $3,$4,$5}'" % v
            output = crash_cmd(crash_process, cmd)
            if output:
                symbol += output[0]

        print("%s %s\t%s" % (v, c, symbol))


def show_usage():
    print("Usage:\n  %s crash vmcore vmlinux slab_name [limit]" % sys.argv[0])
    print("Example:\n"
          "Show top 10 content of the kmalloc-192 slab:\n"
          "  %s crash vmcore vmlinux kmalloc-192 10\n"
          "Show top 20 content:\n"
          "  %s crash /var/crash/127.0.0.1-2020-04-16-23\:16\:56/vmcore "
          "/usr/lib/debug/lib/modules/4.1.12-124.38.1.el7uek.x86_64/vmlinux "
          "kmalloc-192" % (sys.argv[0], sys.argv[0]))


def open_crash_process(args):
    p = subprocess.Popen(args,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=sys.stderr)
    crash_cmd(p, "eval 2")
    return p


def show_slab_info(crash_process, slab_name):
    output = crash_cmd(crash_process, "kmem -s %s" % slab_name)
    print("\n".join(output))

    output = crash_cmd(crash_process, "p nr_online_nodes")
    cnt = int(output[0].split()[-1])

    addr, _ = get_slab_addr_objsize(crash_process, slab_name)

    output = crash_cmd(crash_process, "struct kmem_cache.node %s" % addr)
    nodes = re.findall(r'0x\w+', output[0])[0:cnt]

    print("")
    for i, node in enumerate(nodes):
        output = crash_cmd(crash_process,
                           "struct kmem_cache_node.nr_partial %s" % node)
        nr_partial = int(output[0].split()[-1].rstrip(','))
        print("Number of partially allocated slabs of %s on NUMA node %d: %d" %
              (slab_name, i, nr_partial))
    print("")


def main():
    limit = 20

    if len(sys.argv) < 5 or len(sys.argv) > 6:
        show_usage()
        sys.exit(-1)
    elif len(sys.argv) == 6:
        limit = int(sys.argv[5])

    crash_process = open_crash_process(shlex.split(" ".join(sys.argv[1:4])))
    slab_name = sys.argv[4]

    show_slab_info(crash_process, slab_name)

    content = get_content(crash_process, slab_name)
    counter = Counter()
    for line in content:
        for v in line.split()[1:]:
            counter[v] += 1
    show(crash_process, counter.most_common(limit))
    crash_process.terminate()


if __name__ == '__main__':
    main()
