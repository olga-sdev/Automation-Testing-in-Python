from tests.unit.unit_base_test import UnitBaseTest

from models.item import ItemModel


class ItemTest(UnitBaseTest):  # import UnitBaseTest for better performance
    def test_create_item(self):
        item = ItemModel('test', 19.99)

        self.assertEqual(item.name, 'test',
                         "The name of the item after creation does not equal the constructor argument.")
        self.assertEqual(item.price, 19.99,
                         "The price of the item after creation does not equal the constructor argument.")
        self.assertEqual(item.store_id, 1)
        self.assertIsNone(item.store)
