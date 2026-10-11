from src.catalog import get_low_stock, search_advanced
from src.cart import add_to_cart, cart_total
from src.orders import create_order, save_orders, print_order
from src.analytics import total_revenue
from src.storage import load_products


def main():
    products = load_products('data/products.json')
    print(f"Загружено товаров: {len(products)}")

    low = get_low_stock(products)
    print(f"Товаров с низким остатком: {len(low)}")

    results = search_advanced(products, "Nike")
    print(f"Найдено по запросу 'Nike': {len(results)}")

    cart = []
    ok, msg = add_to_cart(cart, products, 1, '40', 2)
    print(f"Добавление в корзину: {msg}")
    print(f"Сумма корзины: {cart_total(cart)} руб.")

    order = create_order(cart, "Иван Иванов", products)
    print_order(order)

    save_orders([order], "data/orders.json")
    print("Заказ сохранён.")


if __name__ == "__main__":
    main()
