from pymongo import MongoClient

mongo_uri = 'mongodb://localhost'
client = MongoClient(mongo_uri)
db = client['pystock']
users_collection = db['users']


def user_exist(email) -> bool:
    result = users_collection.find_one({"email": email})
    return result is not None


def insert_user(email, password):
    if not user_exist(email):
        users_collection.insert_one({"email": email, "password": password})


def get_password(email):
    return users_collection.find_one({"email": email})["password"]


def get_id(email):
    query = users_collection.find_one({"email": email})
    return query["_id"]


def drop_users():
    users_collection.drop()
