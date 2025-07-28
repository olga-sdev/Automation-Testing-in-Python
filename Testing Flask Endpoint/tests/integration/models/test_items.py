from models.item import ItemModel
from tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        """
        The application context stores information about the app itself, such as configuration and database connections, which are needed during testing but are not inherently created during a test run.
        The app_context() method allows your tests to simulate an environment as if there were requests coming from a user. This is vital for testing functionality that depends on the app being in an "active" state.
        By using self.app_context(), you enable the test to have access to all the necessary components and configurations that the application would normally have when it is running.
        """
        with self.app_context():
            item = ItemModel('test', 14)

            self.assertIsNone(ItemModel.find_by_name('test'))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'))

