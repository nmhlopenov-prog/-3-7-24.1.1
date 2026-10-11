#начало
print("Приложение Чудо обувь запущено")
print("Добро пожаловать!")
login = "admin"
last_name = "Админов"
price = 8990.0
quantity = 5
in_stock = True
#инфа
print("Логин:", login)
print("Фамилия:", last_name)
print("Цена:", price, "руб.")
print("Количество:", quantity)
print("В наличии:", in_stock)
sizes = [36.0, 37.0, 38.0, 39.0]
print("Доступные размеры:")
for size in sizes:
    print("-", size)
print("Номера по порядку:")
for i in range(len(sizes)):
    print(i + 1, "-", sizes[i])
if quantity <= 3:
    print("Мало на складе")
elif quantity <= 10:
    print("Достаточно на складе")
else:
    print("Много на складе")
users = [
    {'login': 'admin', 'last_name': 'Админов', 'role': 'администратор'},
    {'login': 'manager', 'last_name': 'Менеджеров', 'role': 'менеджер'},
    {'login': 'user', 'last_name': 'Пользователев', 'role': 'авторизованный'},
]
for u in users:
    print(f"Логин: {u['login']}, фамилия: {u['last_name']}, роль: {u['role']}")
products = [
    {'id': 1, 'name': 'Air Max', 'price': 8990.0,
     'sizes': {36.0: 2, 37.0: 3, 38.0: 1}},
    {'id': 2, 'name': 'Superstar', 'price': 7490.0,
     'sizes': {37.0: 1, 38.0: 2}},
    {'id': 3, 'name': 'Runfalcon', 'price': 5990.0,
     'sizes': {36.0: 1, 39.0: 4}},
]
for p in products:
    total = sum(p['sizes'].values())
    print(f"{p['name']}: {total} шт., цена {p['price']} руб.")
def find_user(login):
    for u in users:
        if u['login'] == login:
            return u
    return None
result = find_user('admin')
if result:
    print(f"Найден пользователь: {result['last_name']}")
else:
    print("Пользователь не найден")
def total_sum(items):
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total
cart = [
    {'name': 'Air Max', 'price': 8990.0, 'quantity': 2},
    {'name': 'Superstar', 'price': 7490.0, 'quantity': 1},
]
print(f"Итоговая сумма заказа: {total_sum(cart)} руб.")
sorted_by_price = sorted(products, key=lambda p: p['price'])
print("\nТовары по возрастанию цены:")
for p in sorted_by_price:
    print(f"{p['name']} - {p['price']} руб.")
low_stock = [p for p in products if sum(p['sizes'].values()) <= 3]
print("\nТовары с низким остатком (≤ 3 шт.):")
for p in low_stock:
    print(p['name'])
def search_products(query):
    query = query.lower()
    return [p for p in products if query in p['name'].lower()]
found = search_products('max')
print("\nРезультаты поиска 'max':")
for p in found:
    print(p['name'])
def filter_by_price(products, min_price, max_price):
    return [p for p in products if min_price <= p['price'] <= max_price]
result = filter_by_price(products, 5000, 8000)
print("\nТовары от 5000 до 8000 руб.:")
for p in result:
    print(f"{p['name']} — {p['price']} руб.")
def add_to_cart(cart, product, size, quantity):
    cart.append({
        'product': product['name'],
        'price': product['price'],
        'size': size,
        'quantity': quantity,
    })
def remove_from_cart(cart, name):
    cart[:] = [item for item in cart if item['product'] != name]
def change_quantity(cart, name, new_qty):
    for item in cart:
        if item['product'] == name:
            item['quantity'] = new_qty
            break
#аселамалеку
cart = []
add_to_cart(cart, products[0], 36.0, 2)
add_to_cart(cart, products[1], 37.0, 1)
print("\nКорзина:")
for item in cart:
    print(f"{item['product']}, размер {item['size']}, "
          f"{item['quantity']} шт. × {item['price']} = "
          f"{item['quantity'] * item['price']} руб.")
print(f"\nИтого: {total_sum(cart)} руб.")
change_quantity(cart, 'Air Max', 3)
remove_from_cart(cart, 'Superstar')
print("\nПосле изменений:")
for item in cart:
    print(f"{item['product']}, размер {item['size']}, {item['quantity']} шт.")
print(f"Итого: {total_sum(cart)} руб.")
products.append({'id': 4, 'name': 'Zoom Pegasus', 'price': 9990.0,
                 'sizes': {38.0: 2, 39.0: 1, 40.0: 3}})
products.append({'id': 5, 'name': 'Stan Smith', 'price': 6490.0,
                 'sizes': {36.0: 1, 37.0: 1}})
def get_sizes(product):
    return list(product['sizes'].keys())
def get_total_quantity(product):
    return sum(product['sizes'].values())
sorted_by_name = sorted(products, key=lambda p: p['name'])
print("\nТовары по алфавиту:")
for p in sorted_by_name:
    print(p['name'])
cheap = [p for p in products if p['price'] < 6000]
print("\nТовары дешевле 6000 руб.:")
for p in cheap:
    print(f"{p['name']} — {p['price']} руб.")
i = 0
print("\nВсе товары (через while):")
while i < len(products):
    print(products[i]['name'])
    i += 1
orders = [
    {'date': '2026-09-25', 'client': 'Иванов',
     'items': [{'name': 'Air Max', 'price': 8990.0, 'quantity': 1},
               {'name': 'Superstar', 'price': 7490.0, 'quantity': 2}]},
    {'date': '2026-09-20', 'client': 'Петров',
     'items': [{'name': 'Runfalcon', 'price': 5990.0, 'quantity': 1}]},
    {'date': '2026-09-28', 'client': 'Сидоров',
     'items': [{'name': 'Stan Smith', 'price': 6490.0, 'quantity': 3}]},
]
sorted_orders = sorted(orders, key=lambda o: o['date'])
print("\nЗаказы по дате:")
for o in sorted_orders:
    total = sum(i['price'] * i['quantity'] for i in o['items'])
    print(f"{o['date']} — {o['client']} — {total} руб.")