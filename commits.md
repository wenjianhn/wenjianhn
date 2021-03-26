## A list of patches that are backported or wrote by me
### For mainline
commit [3544de8ee6e4](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=3544de8ee6e4) mm, tracing: record slab name for kmem_cache_free()  
commit [91c524708de6](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=91c524708de6) l2tp: copy 4 more bytes to linear part if necessary  
commit [4522a70db7aa](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=4522a70db7aa) l2tp: fix reading optional fields of L2TPv3  
commit [eeb2c4fb6a3d](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=eeb2c4fb6a3d) rds: use DIV_ROUND_UP instead of ceil  
commit [307f39b02199](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=307f39b02199) xen/netfront: remove unnecessary wmb  

### For UEK5 (Based on Linux v4.14.35)
commit [c3687c43800a](https://github.com/oracle/linux-uek/commit/c3687c43800a) genirq/proc: Return proper error code when irq_set_affinity() fails  
commit [a0c32bfb1b54](https://github.com/oracle/linux-uek/commit/a0c32bfb1b54) locking/rwsem: Prevent decrement of reader count before increment  
commit [19a7221ea4e4](https://github.com/oracle/linux-uek/commit/19a7221ea4e4) net: core: another layer of lists, around PF_MEMALLOC skb handling  
commit [7d7f247297a8](https://github.com/oracle/linux-uek/commit/7d7f247297a8) locking/rwsem: Fix (possible) missed wakeup  
commit [2ee51383bd87](https://github.com/oracle/linux-uek/commit/2ee51383bd87) tcp: fix tcp_rtx_queue_tail in case of empty retransmit queue  
commit [5062e2c834b0](https://github.com/oracle/linux-uek/commit/5062e2c834b0) tcp: be more careful in tcp_fragment()  
commit [1fb9eff9e111](https://github.com/oracle/linux-uek/commit/1fb9eff9e111) tcp: refine memory limit test in tcp_fragment()  
commit [d7b8043ee728](https://github.com/oracle/linux-uek/commit/d7b8043ee728) xen/ovmapi: whitelist name_cache for usercopy  
commit [935fa422dff6](https://github.com/oracle/linux-uek/commit/935fa422dff6) l2tp: fix reading optional fields of L2TPv3  
commit [6dac61bfd6db](https://github.com/oracle/linux-uek/commit/6dac61bfd6db) l2tp: copy 4 more bytes to linear part if necessary  

### For UEK4 (Based on Linux v4.1.12)
commit [efb6d4f1cf34](https://github.com/oracle/linux-uek/commit/efb6d4f1cf34) block_dev: don't test bdev->bd_contains when it is not stable  
commit [ea63a6cfb246](https://github.com/oracle/linux-uek/commit/ea63a6cfb246) tcp: fix a stale ooo_last_skb after a replace  
commit [2ad9d506b3da](https://github.com/oracle/linux-uek/commit/2ad9d506b3da) tun: allow positive return values on dev_get_valid_name() call  
commit [1fb814df16a2](https://github.com/oracle/linux-uek/commit/1fb814df16a2) net/mlx4_en: fix potential use-after-free with dma_unmap_page  
commit [2864dd51f2ce](https://github.com/oracle/linux-uek/commit/2864dd51f2ce) crypto: drbg - fix shadow copy of the test buffer  
