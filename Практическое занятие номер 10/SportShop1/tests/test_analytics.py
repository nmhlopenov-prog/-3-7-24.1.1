import unittest
from src import analytics, orders, cart, catalog

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        c = cart.add_to_cart([], catalog.PRODUCTS, 1, 2)
        orders.create_order(c, "Тест")
    def test_total_sales(self):
        self.assertGreater(analytics.total_sales(orders.ORDERS), 0)
    def test_top_products(self):
        top = analytics.top_products(orders.ORDERS, 1)
        self.assertEqual(len(top), 1)
    def test_top_empty(self):
        self.assertEqual(analytics.top_products([], 3), [])

if __name__ == "__main__":
    unittest.main()
