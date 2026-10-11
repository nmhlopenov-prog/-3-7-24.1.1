import unittest
from src import cart, catalog

class TestCart(unittest.TestCase):
    def test_add(self):
        c = cart.add_to_cart([], catalog.PRODUCTS, 1, 2)
        self.assertEqual(len(c), 1)
    def test_remove(self):
        c = cart.add_to_cart([], catalog.PRODUCTS, 1, 2)
        c = cart.remove_from_cart(c, 1)
        self.assertEqual(len(c), 0)
    def test_total(self):
        c = cart.add_to_cart([], catalog.PRODUCTS, 1, 2)
        self.assertEqual(cart.cart_total(c), 3000)
    def test_add_invalid(self):
        with self.assertRaises(ValueError):
            cart.add_to_cart([], catalog.PRODUCTS, 999, 1)

if __name__ == "__main__":
    unittest.main()
