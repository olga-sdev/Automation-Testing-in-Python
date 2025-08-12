import json

from models.store import StoreModel
from models.item import ItemModel
from models.user import UserModel
from tests.base_test import BaseTest


class ItemTest(BaseTest):
    def setUp(self):
        super(ItemTest, self).setUp()
        with self.app() as client:
            with self.app_context():
                UserModel('test', 'pass123').save_to_db()
                auth_request = client.post('/auth',
                                           data=json.dumps({'username': 'test', 'password': 'pass123'}),
                                           headers={'Content-Type': 'application/json'})

                auth_token = json.loads(auth_request.data)['access_token']
                self.access_token = f'JWT {auth_token}'
