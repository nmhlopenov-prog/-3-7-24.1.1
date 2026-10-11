def add_to_cart(cart, products, product_id, quantity):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        raise ValueError("Товар не найден")
    cart.append({"product": product, "quantity": quantity})
    return cart

def remove_from_cart(cart, product_id):
    return [i for i in cart if i["product"]["id"] != product_id]

def cart_total(cart):
    return sum(i["product"]["price"] * i["quantity"] for i in cart)
