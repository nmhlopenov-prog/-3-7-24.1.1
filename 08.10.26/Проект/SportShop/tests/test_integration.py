import unittest
import os
from src.catalog import get_low_stock
from src.cart import add_to_cart, cart_total
from src.orders import create_order, save_orders, load_orders
from src.storage import load_products


class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.products = load_products('data/products.json')
        self.cart = []
        self.orders_file = 'data/test_orders.json'

    def tearDown(self):
        if os.path.exists(self.orders_file):
            os.remove(self.orders_file)

    def test_full_cycle(self):
        result, msg = add_to_cart(self.cart, self.products, 1, '40', 2)
        self.assertTrue(result, msg)

        order = create_order(self.cart, 'Тестовый клиент', self.products)
        self.assertIsNotNone(order)
        self.assertGreater(order['total'], 0)

        save_orders([order], self.orders_file)
        loaded = load_orders(self.orders_file)
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]['total'], order['total'])

    def test_cart_total_matches_order_total(self):
        add_to_cart(self.cart, self.products, 1, '40', 1)
        add_to_cart(self.cart, self.products, 2, '41', 3)
        order = create_order(self.cart, 'Клиент', self.products)
        self.assertIsNotNone(order)
        self.assertEqual(order['total'], cart_total(self.cart))


if __name__ == '__main__':
    unittest.main()
