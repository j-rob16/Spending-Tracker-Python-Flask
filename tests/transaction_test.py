import unittest

from models.transaction import Transaction
from models.merchant import Merchant
from models.product import Product
from models.tag import Tag
from models.user import User

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.user = User('James', 'Rob', 28, 200)
        self.merchant = Merchant('Tesco')
        self.tag = Tag('Groceries')
        self.product = Product('Vegetables', 20)
        self.transaction = Transaction(self.product.price, self.product, self.user, self.merchant)

    def test_transaction_has_price(self):
        self.assertEqual(20, self.transaction.amount)

    def test_transaction_has_product(self):
        self.assertEqual('Vegetables', self.transaction.product.name)

    def test_transaction_has_payer(self):
        self.assertEqual('James', self.transaction.payer.first_name)
        self.assertEqual('Rob', self.transaction.payer.last_name)
        self.assertEqual(28, self.transaction.payer.age)

    def test_transaction_has_merchant(self):
        self.assertEqual('Tesco', self.transaction.payee.name)
