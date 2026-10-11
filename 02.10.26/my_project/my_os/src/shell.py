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
