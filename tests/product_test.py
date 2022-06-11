import unittest

from models.product import Product

class TestProduct(unittest.TestCase):
    
    def setUp(self):
        self.product = Product('Groceries', 50)

    def test_product_has_name(self):
        self.assertEqual('Groceries', self.product.name)

    def test_product_has_price(self):
        self.assertEqual(50)
        