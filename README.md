# Systems Engineering Notes

A personal, evolving collection of study notes and references on operating
systems, infrastructure, performance, and reliability. The material ranges
from Linux kernel internals and hardware behavior to production operations,
distributed-system design, and GPU workloads.

These notes are a working reference rather than a complete or authoritative
guide. Some details and commands are version-specific; check the linked
upstream documentation before relying on them.

## Browse the notes

- **Linux kernel and operating systems** — memory management, scheduling,
  cgroups, filesystems, networking, tracing, crash analysis, and debugging.
  Start with [kernel notes](dev/kernel/), [OS notes](dev/os/), and
  [systemd notes](dev/systemd/).
- **Hardware and performance** — CPU, memory, PCIe, storage, NICs, GPUs,
  reliability/availability/serviceability (RAS), and power. See
  [hardware](dev/hardware/) and [performance](dev/performance/).
- **Networking and system design** — TCP/IP, data-center networking,
  InfiniBand, traffic control, distributed systems, consistency, and
  architecture trade-offs. See [networking](dev/network/),
  [architecture](dev/architecture/), and [algorithms](dev/algorithm/).
- **Kubernetes and containers** — Kubernetes components, cgroups, scheduling,
  observability, troubleshooting, Docker, and containerd. See
  [Kubernetes](dev/k8s/) and [Docker/containerd](dev/docker/).
- **GPU and AI systems** — CUDA, NCCL, PyTorch, GPU profiling and monitoring,
  and performance in multi-GPU and multi-node workloads. See
  [AI and GPU notes](dev/ai/).
- **Reliability and operations** — service-level objectives, monitoring,
  troubleshooting, and operational practices. See [SRE notes](dev/sre/),
  [observability](dev/observability.org), and
  [debugging](dev/debugging/).
- **Languages and tools** — C, Go, Python, compilers, debuggers, allocators,
  and command-line utilities. Browse the [development notes](dev/) and
  [tools](tools/).
- **Career and engineering practice** — career planning, promotion, hiring,
  problem-solving, and principles for making engineering decisions. See
  [career notes](career/), [hiring](hiring.org),
  [sustaining systems](sustaining.org), and [problem-solving](how.org).

## Working with the notes

Most notes are written in Emacs Org-mode (`.org`), with supporting PDFs,
diagrams, and code snippets alongside them. GitHub displays the Org files as
plain text; an Org-mode editor provides the best reading experience.
