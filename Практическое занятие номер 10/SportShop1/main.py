from src import catalog, cart, orders, analytics

def main():
    products = catalog.get_all_products()
    my_cart = []
    while True:
        print("\n=== СПОРТТОВАРЫ ===")
        print("1. Каталог")
        print("2. В корзину")
        print("3. Оформить заказ")
        print("4. Аналитика")
        print("5. Выход")
        choice = input("Выбор: ")
        if choice == "1":
            for p in products:
                print(f"{p['id']}. {p['name']} - {p['price']} руб. (ост. {p['quantity']})")
        elif choice == "2":
            pid = int(input("ID: "))
            qty = int(input("Кол-во: "))
            my_cart = cart.add_to_cart(my_cart, products, pid, qty)
            print("OK")
        elif choice == "3":
            name = input("Имя: ")
            order = orders.create_order(my_cart, name)
            print(f"Заказ {order['id']} на {order['total']} руб.")
            my_cart = []
        elif choice == "4":
            print(f"Продаж: {analytics.total_sales(orders.ORDERS)} руб.")
        elif choice == "5":
            print("Пока!")
            break

if __name__ == "__main__":
    main()
