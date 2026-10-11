ORDERS = []

def create_order(cart, customer_name):
    if not cart:
        raise ValueError("Корзина пуста")
    order = {
        "id": len(ORDERS) + 1,
        "customer": customer_name,
        "items": cart.copy(),
        "total": sum(i["product"]["price"] * i["quantity"] for i in cart),
    }
    ORDERS.append(order)
    return order

def get_order_by_id(order_id):
    for o in ORDERS:
        if o["id"] == order_id:
            return o
    return None
