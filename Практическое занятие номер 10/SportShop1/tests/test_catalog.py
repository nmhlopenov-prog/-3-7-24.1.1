import unittest
from src import catalog

class TestCatalog(unittest.TestCase):
    def test_get_all(self):
        self.assertGreater(len(catalog.get_all_products()), 0)
    def test_get_by_id(self):
        p = catalog.get_product_by_id(1)
        self.assertEqual(p["id"], 1)
    def test_get_by_id_none(self):
        self.assertIsNone(catalog.get_product_by_id(999))
    def test_add_product(self):
        new_id = catalog.add_product("Тест", 100, 1)
        self.assertIsNotNone(catalog.get_product_by_id(new_id))
    def test_low_stock(self):
        low = catalog.get_low_stock(catalog.PRODUCTS)
        for p in low:
            self.assertLessEqual(p["quantity"], 3)

if __name__ == "__main__":
    unittest.main()
