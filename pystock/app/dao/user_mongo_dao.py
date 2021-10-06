from pymongo import MongoClient

mongo_uri = 'mongodb://localhost'
client = MongoClient(mongo_uri)
db = client['pystock']
users_collection = db['users']


def user_exist(email):
    result = users_collection.find_one({"email": email})
    return result is not None


def insert_user(email, password):
    if not user_exist(email):
        users_collection.insert_one({"email": email, "password": password})


def get_password(email):
    return users_collection.find_one({"email": email})["password"]


def get_id(email):
    return str(users_collection.find_one({"email": email})["_id"])


def get_users():

    users_list = []
    for user in users_collection.find({}, {"_id": 0, "password": 0}):
        users_list.append({"email": user["email"]})
    return users_list

def drop_users():
    users_collection.drop()


# Usuario base
insert_user("admin@pystock.com", "1234")
