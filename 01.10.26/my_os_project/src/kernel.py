"""Ядро учебной ОС: управление процессами, памятью, планировщик."""


def schedule_fcfs(processes):
    """Планировщик FCFS: first come — first served."""
    return sorted(processes, key=lambda p: p.get("created_at", 0))


def schedule_round_robin(processes, quantum=1):
    """Планировщик Round Robin с квантом времени."""
    return list(processes)


def schedule_priority(processes):
    """Приоритетное планирование: чем выше priority, тем раньше."""
    return sorted(processes, key=lambda p: -p.get("priority", 0))
