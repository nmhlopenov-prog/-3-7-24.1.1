from src.db import init_db, get_connection
from src.syscalls import sys_echo, sys_get_users, hash_password


BANNER = """
========================================
   my_os — учебная операционная система
   Версия 0.1 | Python + SQLite
========================================
Введите 'help' для списка команд.
"""

HELP = """
Доступные команды:
  help     — показать эту справку
  echo X   — вернуть сообщение X через sys_echo
  users    — список пользователей (sys_get_users)
  adduser  — добавить тестового пользователя
  exit     — завершить работу
"""


def seed_user():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT OR IGNORE INTO users (login, password_hash, role) VALUES (?, ?, ?)",
        ("admin", hash_password("admin123"), "admin"),
    )
    conn.commit()
    conn.close()


def main():
    init_db()
    seed_user()
    print(BANNER)

    while True:
        try:
            cmd = input("my_os> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n[shell] Завершение.")
            break

        if not cmd:
            continue

        parts = cmd.split(maxsplit=1)
        name = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""

        if name == "help":
            print(HELP)

        elif name == "echo":
            print("[kernel]", sys_echo(arg))

        elif name == "users":
            users = sys_get_users()
            if not users:
                print("[kernel] Нет пользователей.")
            else:
                for u in users:
                    print(f"  id={u['id']}  login={u['login']}  role={u['role']}")

        elif name == "adduser":
            seed_user()
            print("[kernel] Тестовый пользователь admin добавлен (если не было).")

        elif name == "exit":
            print("[shell] Завершение работы.")
            break

        else:
            print(f"[shell] Неизвестная команда: {name}")


if __name__ == "__main__":
    main()
