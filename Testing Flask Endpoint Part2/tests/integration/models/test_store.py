from models.item import ItemModel
from models.store import StoreModel
from tests.integration.base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('test')

        self.assertListEqual(store.items.all(), [])
