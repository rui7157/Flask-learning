import unittest
from flask import current_app
from myapp import create_app, db


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.myapp = create_app('test')
        self.app_context = self.myapp.app_context()
        db.create_all()

    def trarDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    # def test_app_is_testing(self):
    #     self.assertTrue(current_app.config['TESTING'])
