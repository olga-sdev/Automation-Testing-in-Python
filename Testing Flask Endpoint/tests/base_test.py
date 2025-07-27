"""
BaseTest

This class is the parent class fro each non-unit test.
It allows instantiation of DB dynamically and makes checks about DB new and blank.
"""

from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    def setUp(self):
        #  Make sure DB exists
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        #  Get test client
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        # DB is cleaned
        with app.app_context():
            db.session.remove()
            db.drop_all()
            
