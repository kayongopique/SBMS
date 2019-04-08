import unittest
from app.models import User


class UserModelTestCase(unittest.TestCase):

    def test_password_setter(self):
        user = User(password = 'dave')
        self.assertTrue(user.password_hash is not None)

    def test_no_read_password(self):
        user = User(password = 'dave')
        with self.assertRaises(AttributeError)
            user.password

    def test_password_verification(self):
        user = User(password = 'dave')
        self.assertTrue(user.verify_password('dave'))
        self.assertFalse(user.verify_password('dav'))

    def test_password_salt_random(self):
        user = User(password = 'dave')
        user2 = User(password = 'dave')
         self.assertTrue(user.password_hash != user2.password_hash)