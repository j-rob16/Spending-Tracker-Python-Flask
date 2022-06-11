import unittest
from models.stock import Stock
from models.merchant import Merchant
from models.product import Product

class TestStock(unittest.TestCase):
    def setUp(self):
        self.merchant = Merchant('Tesco')
        self.product = Product('Vegetables', 20)
        self.stock = Stock(self.product, self.merchant)

    def test_stock_has_product(self):
        self.assertEqual('Vegetables', self.product.name)
        self.assertEqual(20, self.product.price)

    def test_stock_has_merchant(self):
        self.assertEqual('Tesco', self.merchant.name)