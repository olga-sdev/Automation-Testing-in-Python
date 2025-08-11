from models.user import UserModel
from tests.integration.base_test import BaseTest


class UserTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel('test_user', 'password1234')

            self.assertIsNone(UserModel.find_by_username('test_user'))
            self.assertIsNonde(UserModel.find_by_id(1))

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('test_user'))
            self.assertIsNotNonde(UserModel.find_by_id(1))
            
