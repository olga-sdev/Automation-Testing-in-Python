from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('test_user', 'password123')

        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.password, 'password123')
        
