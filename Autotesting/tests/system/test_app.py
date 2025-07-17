import app

from unittest import TestCase
from unittest.mock import patch
from blog import Blog


class AppTest(TestCase):
    def setUp(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
      
