import unittest
from app import Create_app, db
from flask import current_app


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = Create_app('testing') 
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_current_app(self):
        self.assertFalse(current_app is None)

    def test_testing_env(self):
        self.assertTrue(current_app.config['TESTING'])




    




