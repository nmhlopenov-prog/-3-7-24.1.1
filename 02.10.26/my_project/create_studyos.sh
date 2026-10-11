#!/bin/bash
# create_studyos.sh - создаёт проект StudyOS целиком
# Запуск: bash create_studyos.sh

set -e

PROJECT="my_os"

echo "=== Создание проекта $PROJECT ==="
mkdir -p "$PROJECT"/{src,docs,db}
touch "$PROJECT/src/__init__.py"

# ---------- db.py ----------
cat > "$PROJECT/src/db.py" << 'PYEOF'
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'db', 'os.sqlite')

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS syscalls_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            syscall_name TEXT NOT NULL,
            args TEXT,
            user TEXT,
            status TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT 'user'
        );
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT UNIQUE NOT NULL,
            content TEXT,
            owner TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS processes (
            pid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            state TEXT DEFAULT 'running',
            owner TEXT,
            memory INTEGER DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)
    cur.execute("SELECT COUNT(*) FROM users WHERE login = 'admin'")
    if cur.fetchone()[0] == 0:
        cur.execute(
            "INSERT INTO users (login, password_hash, role) VALUES (?, ?, ?)",
            ('admin', 'secret', 'admin')
        )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("База данных инициализирована:", DB_PATH)
PYEOF

# ---------- syscalls.py ----------
cat > "$PROJECT/src/syscalls.py" << 'PYEOF'
from src.db import get_connection

def log_syscall(name, args="", user="system", status="OK"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO syscalls_log (syscall_name, args, user, status) VALUES (?, ?, ?, ?)",
        (name, args, user, status)
    )
    conn.commit()
    conn.close()

def sys_login(login, password, current_user="guest"):
    log_syscall("sys_login", login, current_user)
    return True

def sys_logout(current_user="guest"):
    log_syscall("sys_logout", "", current_user)
    return True

def sys_whoami(current_user="guest"):
    log_syscall("sys_whoami", "", current_user)
    return current_user

def sys_create_file(path, content, current_user="guest"):
    log_syscall("sys_create_file", path, current_user)
    return 1

def sys_read_file(path, current_user="guest"):
    log_syscall("sys_read_file", path, current_user)
    return ""

def sys_delete_file(path, current_user="guest"):
    log_syscall("sys_delete_file", path, current_user)
    return True

def sys_list_files(path, current_user="guest"):
    log_syscall("sys_list_files", path, current_user)
    return []

def sys_exec(program, current_user="guest"):
    log_syscall("sys_exec", program, current_user)
    return 42

def sys_ps(current_user="guest"):
    log_syscall("sys_ps", "", current_user)
    return []

def sys_kill(pid, current_user="guest"):
    log_syscall("sys_kill", str(pid), current_user)
    return True

def sys_mem_alloc(size, current_user="guest"):
    log_syscall("sys_mem_alloc", str(size), current_user)
    return 0

def sys_logs(current_user="guest"):
    log_syscall("sys_logs", "", current_user)
    return []

def sys_shutdown(current_user="guest"):
    log_syscall("sys_shutdown", "", current_user)
    return True

if __name__ == "__main__":
    print(sys_login("admin", "secret"))
    print(sys_whoami("admin"))
    print(sys_create_file("/test.txt", "hello", "admin"))
    print(sys_ps("admin"))
PYEOF

# ---------- shell.py ----------
cat > "$PROJECT/src/shell.py" << 'PYEOF'
from src.syscalls import (
    sys_login, sys_logout, sys_whoami,
    sys_create_file, sys_list_files, sys_ps, sys_logs
)

def main():
    current_user = "guest"
    print("StudyOS Shell v0.2")
    print("Команды: whoami, login, logout, create, ls, ps, logs, exit")

    while True:
        prompt = f"{current_user}@studyos:~$ "
        try:
            cmd = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if cmd == "exit":
            break
        elif cmd == "whoami":
            print(sys_whoami(current_user))
        elif cmd == "login":
            login = input("Логин: ")
            password = input("Пароль: ")
            if sys_login(login, password, current_user):
                current_user = login
                print(f"Вы вошли как {login}")
            else:
                print("Ошибка входа")
        elif cmd == "logout":
            sys_logout(current_user)
            current_user = "guest"
            print("Вы вышли из системы")
        elif cmd == "create":
            path = input("Путь: ")
            content = input("Содержимое: ")
            fid = sys_create_file(path, content, current_user)
            print(f"Создан файл с id={fid}")
        elif cmd == "ls":
            files = sys_list_files("/", current_user)
            for f in files:
                print(f)
        elif cmd == "ps":
            processes = sys_ps(current_user)
            for p in processes:
                print(p)
        elif cmd == "logs":
            entries = sys_logs(current_user)
            for e in entries:
                print(e)
        else:
            print(f"Команда не найдена: {cmd}")

if __name__ == "__main__":
    main()
PYEOF

# ---------- config.py ----------
cat > "$PROJECT/src/config.py" << 'PYEOF'
DB_PATH = "db/os.sqlite"
MAX_PROCESSES = 10
MAX_MEMORY = 1024
HASH_ALGO = "sha256"
PYEOF

# ---------- kernel.py ----------
cat > "$PROJECT/src/kernel.py" << 'PYEOF'
# Заготовка ядра StudyOS

def enqueue_process(process):
    return True

def set_priority(pid, priority):
    return True

def allocate_memory(pid, size):
    return 0
PYEOF

# ---------- docs/02_OS_Architecture.md ----------
cat > "$PROJECT/docs/02_OS_Architecture.md" << 'MDEOF'
# Архитектура учебной операционной системы StudyOS

## 1. Список модулей ОС

- shell.py - оболочка, принимает команды пользователя.
- syscalls.py - системные вызовы, логирует вызовы.
- kernel.py - ядро, управляет ресурсами.
- scheduler.py - планировщик процессов.
- memory.py - менеджер памяти.
- fs.py - файловая система.
- auth.py - аутентификация и права.
- db.py - база данных SQLite.

## 2. Спецификация системных вызовов

- sys_login(login, password, current_user="guest") -> bool
- sys_logout(current_user="guest") -> bool
- sys_whoami(current_user="guest") -> str
- sys_create_file(path, content, current_user="guest") -> int
- sys_read_file(path, current_user="guest") -> str
- sys_delete_file(path, current_user="guest") -> bool
- sys_list_files(path, current_user="guest") -> list
- sys_exec(program, current_user="guest") -> int
- sys_ps(current_user="guest") -> list
- sys_kill(pid, current_user="guest") -> bool
- sys_mem_alloc(size, current_user="guest") -> int
- sys_logs(current_user="guest") -> list
- sys_shutdown(current_user="guest") -> bool

## 3. Контракты функций

### sys_create_file
- Предварительное условие: пользователь авторизован.
- Постусловие: файл создан, возвращён его id.
- Побочный эффект: запись в syscalls_log.

### sys_login
- Предварительное условие: пользователь с таким логином есть в базе.
- Постусловие: возвращено True или False.
- Побочный эффект: запись в syscalls_log.

### sys_delete_file
- Предварительное условие: файл существует, пользователь авторизован.
- Постусловие: файл удалён, возвращено True.
- Побочный эффект: запись в syscalls_log.

## 4. Структуры данных

process = {
    'pid': 1,
    'name': 'shell',
    'state': 'running',
    'owner': 'admin',
    'memory': 120,
    'created_at': '2025-01-01 10:00:00'
}

file = {
    'id': 1,
    'path': '/home/test.txt',
    'content': 'hello',
    'owner': 'admin',
    'created_at': '2025-01-01 10:00:00'
}

user = {
    'id': 1,
    'login': 'admin',
    'password_hash': 'abc123...',
    'role': 'admin'
}

log = {
    'id': 1,
    'syscall_name': 'sys_login',
    'args': 'admin',
    'user': 'admin',
    'status': 'OK',
    'timestamp': '2025-01-01 10:00:00'
}
MDEOF

# ---------- Инициализация БД ----------
echo ""
echo "=== Инициализация базы данных ==="
cd "$PROJECT"
python3 -m src.db

echo ""
echo "=== Готово! Структура проекта: ==="
find . -type f | sort
echo ""
echo "Запуск:"
echo "  cd $PROJECT"
echo "  python3 -m src.syscalls"
echo "  python3 -m src.shell"
