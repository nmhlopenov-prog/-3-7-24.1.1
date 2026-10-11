def add_to_cart(cart, products, product_id, size, quantity):
    """Добавляет товар в корзину."""
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        return False, "Товар не найден"
    if size not in product.get('sizes', {}):
        return False, "Неверный размер"
    if product['sizes'][size] < quantity:
        return False, "Недостаточно товара"

    for item in cart:
        if item['id'] == product_id and item['size'] == size:
            item['quantity'] += quantity
            return True, "Количество увеличено"

    cart.append({
        'id': product_id,
        'name': product['name'],
        'price': product['price'],
        'size': size,
        'quantity': quantity
    })
    return True, "Товар добавлен"


def remove_from_cart(cart, product_id, size):
    """Удаляет позицию из корзины."""
    for i, item in enumerate(cart):
        if item['id'] == product_id and item['size'] == size:
            del cart[i]
            return True
    return False


def update_quantity(cart, products, product_id, size, new_qty):
    """Изменяет количество товара в корзине."""
    if new_qty <= 0:
        return remove_from_cart(cart, product_id, size)
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        return False
    if product['sizes'].get(size, 0) < new_qty:
        return False
    for item in cart:
        if item['id'] == product_id and item['size'] == size:
            item['quantity'] = new_qty
            return True
    return False


def cart_total(cart):
    """Сумма корзины."""
    return sum(item['price'] * item['quantity'] for item in cart)
