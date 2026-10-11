import os

def build():
    print("Сборка...")
    os.system("python3 -m unittest discover -s tests")
    print("Готово.")

if __name__ == "__main__":
    build()
