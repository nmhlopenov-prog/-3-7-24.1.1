import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "db", "os.sqlite")
MAX_PROCESSES = 10
MAX_MEMORY_MB = 64
SYSCALL_TIME_LIMIT_MS = 50
