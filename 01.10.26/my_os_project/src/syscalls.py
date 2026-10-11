import hashlib
from src.db import get_connection


def log_syscall(name, args="", user="system", status="ok"):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO syscalls_log (syscall, args, user, status) VALUES (?, ?, ?, ?)",
        (name, str(args), user, status),
    )
    conn.commit()
    conn.close()


def sys_echo(message):
    log_syscall("sys_echo", message)
    return message


def sys_get_users():
    log_syscall("sys_get_users")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, login, role FROM users")
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()
