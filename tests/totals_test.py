import unittest

from models.total import Total
from models.user import User
from models.merchant import Merchant

class TestTotal(unittest.TestCase):
    def setUp(self):
        self.user = User('James', 'Rob', 28, 200)
        self.merchant = Merchant('Tesco')
        self.total = Total(1000, self.user, self.merchant)

    def test_total_has_total_paid_to_merchant(self):
        self.assertEqual(1000, self.total.total_paid)

    def test_total_has_user(self):
        self.assertEqual('James', self.total.user.first_name)

    def test_total_has_merchant(self):
        self.assertEqual('Tesco', self.total.merchant.name)