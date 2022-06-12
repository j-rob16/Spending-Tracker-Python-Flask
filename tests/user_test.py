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

    def test_update_first_name(self):
        self.user.update_first_name('Jack')
        self.assertEqual('Jack', self.user.first_name)

    def test_update_last_name(self):
        self.user.update_last_name('Smith')
        self.assertEqual('Smith', self.user.last_name)

    def test_add_to_wallet(self):
        self.user.add_to_wallet(100)
        self.assertEqual(300, self.user.wallet)