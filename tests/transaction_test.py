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
        self.transaction = Transaction(self.product, self.user, self.merchant, self.tag)

    def test_transaction_has_price(self):
        self.assertEqual(20, self.transaction.product.price)

    def test_transaction_has_product(self):
        self.assertEqual('Vegetables', self.transaction.product.name)

    def test_transaction_has_payer(self):
        self.assertEqual('James', self.transaction.user.first_name)
        self.assertEqual('Rob', self.transaction.user.last_name)
        self.assertEqual(28, self.transaction.user.age)

    def test_transaction_has_merchant(self):
        self.assertEqual('Tesco', self.transaction.merchant.name)

    def test_transaction_has_tag(self):
        self.assertEqual('Groceries', self.transaction.tag.category)

    def test_user_pays_for_product(self):
        self.transaction.money_transfer()
        self.assertEqual(180, self.user.wallet)
