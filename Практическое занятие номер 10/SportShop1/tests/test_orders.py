import unittest
from src import orders, cart, catalog

class TestOrders(unittest.TestCase):
    def test_create(self):
        c = cart.add_to_cart([], catalog.PRODUCTS, 1, 1)
        o = orders.create_order(c, "Иван")
        self.assertEqual(o["customer"], "Иван")
    def test_empty_cart(self):
        with self.assertRaises(ValueError):
            orders.create_order([], "Иван")
    def test_get_by_id(self):
        c = cart.add_to_cart([], catalog.PRODUCTS, 1, 1)
        o = orders.create_order(c, "Пётр")
        self.assertEqual(orders.get_order_by_id(o["id"])["customer"], "Пётр")

if __name__ == "__main__":
    unittest.main()
