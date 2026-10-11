import unittest
import os
from src import storage

class TestStorage(unittest.TestCase):
    def test_save_load(self):
        data = [{"id": 1, "name": "Тест"}]
        storage.save_data(data, "/tmp/test_data.json")
        loaded = storage.load_data("/tmp/test_data.json")
        self.assertEqual(loaded, data)
        os.remove("/tmp/test_data.json")
    def test_load_missing(self):
        with self.assertRaises(FileNotFoundError):
            storage.load_data("/tmp/no_such_file.json")

if __name__ == "__main__":
    unittest.main()
