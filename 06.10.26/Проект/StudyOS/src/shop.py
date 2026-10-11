"""Модуль работы с товарами магазина SportShop."""


def get_low_stock(products, threshold=5):
    """Возвращает список товаров с количеством ниже порога."""
    return [p for p in products if p.get("quantity", 0) < threshold]


def total_sum(products):
    return sum(p['price'] * p['quantity'] for p in products)


def search_advanced(products, query, category=None, min_price=None, max_price=None):
    """Расширенный поиск товаров по названию, категории и цене."""
    result = []
    for p in products:
        if query.lower() not in p.get('name', '').lower():
            continue
        if category and p.get('category') != category:
            continue
        if min_price is not None and p['price'] < min_price:
            continue
        if max_price is not None and p['price'] > max_price:
            continue
        result.append(p)
    return result


def cart_total(cart):
    return sum(item['price'] * item['quantity'] for item in cart)
