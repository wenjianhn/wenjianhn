# Unaccounted pages of sriov
```shellsession
# echo 0 > /sys/class/net/re0/device/sriov_numvfs
# perf record -a -e kmem:mm_page_alloc -e kmem:mm_page_alloc_zone_locked -g --exclude-perf echo 24 > /sys/class/net/re0/device/sriov_numvfs

# perf script -i perf.data > set_24_vfs.perf
# ./mem_by_stack.py set_24_vfs.perf > set_24_vfs.perf.result

# head -20 set_24_vfs.perf.result
Allocated 17029 MiB by
	ffffffffad1e24eb __alloc_pages_nodemask ([kernel.kallsyms])
		    b0b0 give_pages ([mlx5_core])
		    b497 pages_work_handler ([mlx5_core])
	ffffffffad0b18b9 process_one_work ([kernel.kallsyms])
	ffffffffad0b236d worker_thread ([kernel.kallsyms])
	ffffffffad0b8005 kthread ([kernel.kallsyms])
	ffffffffada00344 ret_from_fork ([kernel.kallsyms])

Allocated 17002 MiB by
	ffffffffad1e051c __rmqueue ([kernel.kallsyms])
	ffffffffad1e1b3b get_page_from_freelist ([kernel.kallsyms])
	ffffffffad1e23e3 __alloc_pages_nodemask ([kernel.kallsyms])
		    b0b0 give_pages ([mlx5_core])
		    b497 pages_work_handler ([mlx5_core])
	ffffffffad0b18b9 process_one_work ([kernel.kallsyms])
	ffffffffad0b236d worker_thread ([kernel.kallsyms])
	ffffffffad0b8005 kthread ([kernel.kallsyms])
	ffffffffada00344 ret_from_fork ([kernel.kallsyms])

```
