import json

def save_data(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return True

def load_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
