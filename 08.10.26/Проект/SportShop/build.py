import subprocess
import sys
import os


def check_python_version():
    if sys.version_info < (3, 10):
        print("Требуется Python 3.10+")
        sys.exit(1)
    print(f"Python {sys.version.split()[0]} — OK")


def check_data():
    if not os.path.exists("data/products.json"):
        print("Файл данных не найден!")
        sys.exit(1)
    print("Файл данных найден — OK")


def run_tests():
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        capture_output=True, text=True
    )
    print(result.stdout)
    if result.returncode != 0:
        print("Тесты не прошли!")
        sys.exit(1)
    print("Все тесты пройдены — OK")


def run_app():
    print("Запуск main.py...")
    subprocess.run([sys.executable, "main.py"])


if __name__ == "__main__":
    check_python_version()
    check_data()
    run_tests()
    print("Сборка успешна!")
    run_app()
