import json
import os
from datetime import datetime

# ---------- Данные ----------
PRODUCTS = [
    {"id": 1, "name": "Мяч футбольный",   "brand": "Adidas", "category": "Футбол",   "price": 2500, "qty": 2},
    {"id": 2, "name": "Кроссовки беговые","brand": "Nike",   "category": "Обувь",    "price": 8900, "qty": 10},
    {"id": 3, "name": "Гантели 5 кг",     "brand": "Sport",  "category": "Фитнес",   "price": 1200, "qty": 1},
    {"id": 4, "name": "Скакалка",         "brand": "Sport",  "category": "Фитнес",   "price": 450,  "qty": 15},
    {"id": 5, "name": "Мяч баскетбольный","brand": "Wilson", "category": "Баскетбол","price": 3200, "qty": 3},
]

# ---------- US-1: товары с низким остатком ----------
def get_low_stock(products, threshold=3):
    low = [p for p in products if p["qty"] <= threshold]
    return sorted(low, key=lambda p: p["qty"])

def highlight_low_stock(products):
    low = get_low_stock(products)
    if not low:
        print("Нет товаров с низким остатком")
        return
    print(f"{'ID':<4}{'Название':<25}{'Бренд':<10}{'Кол-во':<8}")
    print("-" * 50)
    for p in low:
        print(f"{p['id']:<4}{p['name']:<25}{p['brand']:<10}{p['qty']:<8}")

# ---------- US-2: расширенный поиск ----------
def search_advanced(products, query, category=None, min_price=None, max_price=None):
    q = query.lower() if query else ""
    result = []
    for p in products:
        if q and (q not in p["name"].lower() and q not in p["brand"].lower()):
            continue
        if category and p["category"] != category:
            continue
        if min_price is not None and p["price"] < min_price:
            continue
        if max_price is not None and p["price"] > max_price:
            continue
        result.append(p)
    return result

# ---------- US-3: аналитика по категориям ----------
def count_by_category(products):
    result = {}
    for p in products:
        result[p["category"]] = result.get(p["category"], 0) + 1
    return result

def total_stock_value(products):
    return sum(p["price"] * p["qty"] for p in products)

# ---------- US-4: заказы и JSON ----------
def create_order(products, items):
    order_items = []
    total = 0
    for it in items:
        prod = next((p for p in products if p["id"] == it["id"]), None)
        if prod is None:
            continue
        qty = min(it["qty"], prod["qty"])
        if qty <= 0:
            continue
        subtotal = prod["price"] * qty
        order_items.append({
            "id": prod["id"],
            "name": prod["name"],
            "qty": qty,
            "price": prod["price"],
            "subtotal": subtotal,
        })
        total += subtotal
    return {
        "date": datetime.now().isoformat(timespec="seconds"),
        "items": order_items,
        "total": total,
    }

def save_orders(orders, filename="orders.json"):
    existing = load_orders(filename)
    existing.extend(orders)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    return filename

def load_orders(filename="orders.json"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

# ---------- US-5: журнал действий ----------
def log_action(user, action, details=""):
    with open("actions.log", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat(timespec='seconds')} | {user} | {action} | {details}\n")

# ---------- Меню ----------
def main():
    user = "manager"
    while True:
        print("\n=== СпортТовары ===")
        print("1. Показать товары с низким остатком (US-1)")
        print("2. Поиск (US-2)")
        print("3. Аналитика (US-3)")
        print("4. Оформить заказ (US-4)")
        print("5. Журнал (US-5)")
        print("0. Выход")
        choice = input("Выбор: ").strip()

        if choice == "1":
            highlight_low_stock(PRODUCTS)
            log_action(user, "low_stock", "")
        elif choice == "2":
            q = input("Запрос: ").strip()
            cat = input("Категория (Enter — пропустить): ").strip() or None
            res = search_advanced(PRODUCTS, q, category=cat)
            for p in res:
                print(p)
            log_action(user, "search", f"q={q}, cat={cat}")
        elif choice == "3":
            print("По категориям:", count_by_category(PRODUCTS))
            print("Стоимость склада:", total_stock_value(PRODUCTS))
            log_action(user, "analytics", "")
        elif choice == "4":
            pid = int(input("ID товара: "))
            qty = int(input("Количество: "))
            order = create_order(PRODUCTS, [{"id": pid, "qty": qty}])
            save_orders([order])
            print(f"Заказ сохранён. Сумма: {order['total']}")
            log_action(user, "order", f"id={pid}, qty={qty}")
        elif choice == "5":
            if os.path.exists("actions.log"):
                with open("actions.log", "r", encoding="utf-8") as f:
                    print(f.read())
            else:
                print("Журнал пуст")
        elif choice == "0":
            break

if __name__ == "__main__":
    main()
