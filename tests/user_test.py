import unittest

from models.user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User('James', 'Rob', 28, 200)

    def test_user_has_first_name(self):
        self.assertEqual('James', self.user.first_name)

    def test_user_has_last_name(self):
        self.assertEqual('Rob', self.user.last_name)

    def test_user_has_age(self):
        self.assertEqual(28, self.user.age)

    def test_user_has_wallet(self):
        self.assertEqual(200, self.user.wallet)