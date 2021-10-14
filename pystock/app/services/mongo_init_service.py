from pymongo import MongoClient


def create_instance():
    mongo_uri = 'mongodb://localhost'
    client = MongoClient(mongo_uri)
    return client['pystock']


class MongoInitService:

    def __init__(self):
        # -- DB Creation --
        self._db = create_instance()

        # -- Collections --
        self._users_collection = self._create_collection('users')
        self._products_collection = self._create_collection('products')

        # -- Base Data --
        # Admin User
        self._users_collection.insert_one({"email": "admin@pystock.com", "password": "1234"})

    def _create_collection(self, name):
        return self._db[name]

    # Collections Getters
    def get_users(self):
        return self._users_collection

    def get_products(self):
        return self._products_collection
