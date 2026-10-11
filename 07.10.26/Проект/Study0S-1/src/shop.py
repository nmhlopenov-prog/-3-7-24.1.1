"""Модуль работы с товарами и корзиной магазина SportShop."""


def _total_quantity(product):
    """Общее количество товара (по quantity или по sizes)."""
    if "quantity" in product:
        return product["quantity"]
    if "sizes" in product:
        return sum(product["sizes"].values())
    return 0


def get_low_stock(products, threshold=5):
    """Товары с суммарным количеством ниже порога."""
    return [p for p in products if _total_quantity(p) < threshold]


def total_sum(products):
    """Сумма стоимости товаров с учётом количества."""
    return sum(p["price"] * _total_quantity(p) for p in products)


def search_advanced(products, query, category=None, min_price=None, max_price=None):
    """Расширенный поиск товаров по названию, категории и цене."""
    result = []
    for p in products:
        if query.lower() not in p.get("name", "").lower():
            continue
        if category and p.get("category") != category:
            continue
        if min_price is not None and p.get("price", 0) < min_price:
            continue
        if max_price is not None and p.get("price", 0) > max_price:
            continue
        result.append(p)
    return result


def add_to_cart(cart, products, product_id, size, quantity=1):
    """Добавляет товар в корзину. Возвращает (result, message)."""
    product = next((p for p in products if p.get("id") == product_id), None)
    if product is None:
        return False, "Товар не найден"
    sizes = product.get("sizes", {})
    if size not in sizes:
        return False, f"Размер {size} не найден"
    if quantity <= 0:
        return False, "Количество должно быть положительным"
    if sizes[size] < quantity:
        return False, "Недостаточно товара на складе"
    for item in cart:
        if item["id"] == product_id and item["size"] == size:
            item["quantity"] += quantity
            return True, "Количество увеличено"
    cart.append({
        "id": product_id,
        "name": product["name"],
        "size": size,
        "price": product["price"],
        "quantity": quantity,
    })
    return True, "Товар добавлен"


def remove_from_cart(cart, product_id, size):
    """Удаляет позицию из корзины."""
    for i, item in enumerate(cart):
        if item["id"] == product_id and item["size"] == size:
            del cart[i]
            return True
    return False


def update_quantity(cart, product_id, size, quantity):
    """Меняет количество позиции в корзине."""
    if quantity <= 0:
        return remove_from_cart(cart, product_id, size)
    for item in cart:
        if item["id"] == product_id and item["size"] == size:
            item["quantity"] = quantity
            return True
    return False


def cart_total(cart):
    """Сумма корзины с учётом количества."""
    return sum(item["price"] * item["quantity"] for item in cart)
