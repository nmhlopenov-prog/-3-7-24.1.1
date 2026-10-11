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
