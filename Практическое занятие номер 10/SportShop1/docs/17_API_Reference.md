# API Reference — СпортТовары

## catalog.py
### get_all_products()
Возвращает список всех товаров из каталога.
### get_product_by_id(product_id)
Возвращает товар по ID.
### add_product(name, price, quantity)
Добавляет новый товар.
### get_low_stock(products)
Возвращает товары с количеством ≤ 3.

## cart.py
### add_to_cart(cart, products, product_id, quantity)
### remove_from_cart(cart, product_id)
### cart_total(cart)

## orders.py
### create_order(cart, customer_name)
### get_order_by_id(order_id)

## analytics.py
### total_sales(orders)
### top_products(orders, n=5)

## storage.py
### save_data(data, filename)
### load_data(filename)
