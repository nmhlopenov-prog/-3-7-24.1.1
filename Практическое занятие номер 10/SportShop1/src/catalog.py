PRODUCTS = [
    {"id": 1, "name": "Футбольный мяч", "price": 1500, "quantity": 10},
    {"id": 2, "name": "Баскетбольный мяч", "price": 2000, "quantity": 5},
    {"id": 3, "name": "Гантели 5кг", "price": 1200, "quantity": 2},
    {"id": 4, "name": "Скакалка", "price": 300, "quantity": 20},
    {"id": 5, "name": "Коврик для йоги", "price": 800, "quantity": 3},
]

def get_all_products():
    return PRODUCTS

def get_product_by_id(product_id):
    for p in PRODUCTS:
        if p["id"] == product_id:
            return p
    return None

def add_product(name, price, quantity):
    new_id = max(p["id"] for p in PRODUCTS) + 1
    PRODUCTS.append({"id": new_id, "name": name, "price": price, "quantity": quantity})
    return new_id

def get_low_stock(products):
    return [p for p in products if p["quantity"] <= 3]
