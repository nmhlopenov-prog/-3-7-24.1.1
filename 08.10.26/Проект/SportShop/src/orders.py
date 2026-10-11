import json
import os


def create_order(cart, client_name, products):
    """Создаёт заказ на основе корзины."""
    if not cart:
        return None
    total = sum(item['price'] * item['quantity'] for item in cart)
    order = {
        'client': client_name,
        'items': [dict(item) for item in cart],
        'total': total
    }
    return order


def print_order(order):
    """Печатает заказ."""
    if order is None:
        print("Заказ пуст")
        return
    print(f"Клиент: {order['client']}")
    for item in order['items']:
        print(f"  {item['name']} (размер {item['size']}) "
              f"x{item['quantity']} = "
              f"{item['price'] * item['quantity']} руб.")
    print(f"Итого: {order['total']} руб.")


def save_orders(orders, filename):
    """Сохраняет заказы в JSON."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(orders, f, ensure_ascii=False, indent=2)


def load_orders(filename):
    """Загружает заказы из JSON."""
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
