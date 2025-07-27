from unittest import TestCase

from starter_code.models.item import ItemModel


class ItemTest(TestCase):
    def test_create_item(self):
        # usually is not tested because it's simple
        item = ItemModel('test', 14)

        self.assertEqual(item.name, 'test', "The name of the item does not match the constructor arg")
        self.assertEqual(item.price, 14, "The price of the item does not match the constructor arg")

    def test_item_json(self):
        item = ItemModel('test', 14)
        expected = {
            'name': 'test',
            'price': 14
        }

        self.assertEqual(item.json(), expected,
                         "The JSON export of the item is wrong."
                         f"Received {item.json()} and expected is {expected}")
        
