#!/usr/bin/env python

from __future__ import print_function

import sys
from collections import Counter


def get_order(head):
    h = head.split()
    for i in h:
        if i.startswith("order="):
            return int(i.split('=')[1])


def main():
    if len(sys.argv) < 2:
        print("Usage:\n  %s <perf_script_output_file>" % sys.argv[0], file=sys.stderr)
        sys.exit(-1)

    counter = Counter()
    order = -1
    trace = ''

    with open(sys.argv[1]) as f:
        for line in f:
            if order == -1:
                order = get_order(line)
            elif line == '\n':
                counter[trace] += 4096L << order
                print(trace, counter[trace])
                order = -1
                trace = ''
            else:
                trace += line

    for t, b in counter.most_common():
        print("Freed/Allocated %d MiB by\n%s" % (b/1024/1024, t))


if __name__ == '__main__':
    main()
