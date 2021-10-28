# The mlx4_ib module looks suspicious
```shellsession
$ time ./slab_content_top.py crash_dom0_domU /sr/path/vmcore.gz_127968163/this/vmcore  /sr/path/vmcore.gz_127968163/this/vmlinux kmalloc-192
CACHE            NAME                 OBJSIZE  ALLOCATED     TOTAL  SLABS  SSIZE
ffff8802a6401800 kmalloc-192              192   10830265  10830330  515730     4k

Number of partially allocated slabs on NUMA node 0: 0

Content          Count  Symbol/Slab
0000000000000000 3627670
0000000000000001 545399
ffffffffffffffff 516985
ffffffff8109f0d0 515177 delayed_work_timer_fn /usr/src/debug/kernel-4.1.12/linux-4.1.12-124.26.12.el6uek/kernel/workqueue.c: 1464
ffff8800734d0000 515149
ffffffffc02e60e0 515143 id_map_ent_timeout [mlx4_ib]
0000000fffffffe0 515118
ffff8802a6406000 173669 kmalloc-512
ffffffff82026582 157349 boot_tvec_bases+2
ffff8802c6e91882 150976
dead000000000200 138150
ffff8802c6ed1882 104633
ffff8802c6e51882 102185
0000000000000002 43049
0000000000000003 31086
ffffffff81771ea0 13021  proc_bus_pci_devices_op
ffffffff81741220 12942  kernfs_seq_ops
2020202020202020 12050
ffffea0000000000 4090
ffffea0000000002 3796

real    8m22.582s
user    1m35.809s
sys     5m8.359s
```

# kmalloc-128 of /proc/kcore
```shellsession
$ sudo ./slab_content_top.py ~/code/github.com/crash-utility/crash/crash /proc/kcore /usr/lib/debug/boot/vmlinux-4.15.0-159-generic kmalloc-128 100
CACHE             OBJSIZE  ALLOCATED     TOTAL  SLABS  SSIZE  NAME
ffff8e13f5c03500      128      43384     43584   1362     4k  kmalloc-128

Number of partially allocated slabs of kmalloc-128 on NUMA node 0: 0

Content          Count	Symbol/Slab
0000000000000000 4869
4e455f4b454e465f 967
3551455a5941504e 948
2e44455450595243 948
30326c736c324776 948
47774b7859565a68 948
5346545059524345 948
75326572775a5846 551
75326572775a5746 397
0000000000000020 329
0000000000000100 328
ffffffff95840720 327	crypto_skcipher_exit_tfm /build/linux-teTg6M/linux-4.15.0/crypto/skcipher.c: 822
ffffffff95841ae0 327
0000005800000010 172
ffffffffc0c95120 172	simd_skcipher_encrypt [crypto_simd]
ffff8e13ec375248 172	kmalloc-512
ffffffffc0c95050 172	simd_skcipher_decrypt [crypto_simd]
0000000000000001 164
0000000800000010 155
ffffffffc0ca5a90 155	cryptd_skcipher_decrypt_enqueue [cryptd]
ffffffffc0ca5ad0 155	cryptd_skcipher_encrypt_enqueue [cryptd]
ffff8e13e8ae6c48 155	kmalloc-1024
726d756d48474150 55
776d465738687336 55
504a62394362567a 55
ffffffffc04a5b90 34	release_crtc_commit [drm_kms_helper]
0000000000001000 19
dead000000000100 17
ffffffffffffffff 15
000003e8000003e8 13
000001fe00000000 13
000081a400000000 10
0000000000000068 10
ffff8e136a93f040 9	ip4-frags
00000000617a02a5 9
ffffffff9685af80 9	init_pid_ns
00000000617a0297 9
ffffffffc04f44a0 8	irq_i915_sw_fence_work [i915]
00000000617a02b3 8
000000002d2d6b50 8
000041ed00000000 7
0000000200000003 7
69625f7374736964 7
5f75746e7562755f 7
ffffffff9569da50 7	__d_free_external_name /build/linux-teTg6M/linux-4.15.0/fs/dcache.c: 274
2e73726f7272696d 7
6d6f632e39396e63 7
00000000617a02ae 6
00000000617a02a2 6
00000000617a02a3 6
000000002d2d454d 6
4232706476557762 6
000000002d2d6b7a 6
00000000617a030c 6
ffffffff956146c0 6	tlb_remove_table_rcu /build/linux-teTg6M/linux-4.15.0/mm/memory.c: 380
```
