from pymongo import MongoClient
from bson.objectid import ObjectId

mongo_uri = 'mongodb://localhost'
client = MongoClient(mongo_uri)
db = client['pystock']
users_collection = db['users']


def user_exist(email):
    result = users_collection.find_one({"email": email})
    return result is not None


def get_password(email):
    return users_collection.find_one({"email": email})["password"]


def get_id(email):
    return str(users_collection.find_one({"email": email})["_id"])


def insert_user(email, password):
    if not user_exist(email):
        response = users_collection.insert_one({"email": email, "password": password})
        return({
            "id": str(response.inserted_id),
            "email": email
        })


def get_users():
    users = []
    for user in users_collection.find({}):
        users.append(
            {
                "id": str(user["_id"]),
                "email": user["email"]
            })
    return users


def delete_user(user_id):
    users_collection.delete_one({"_id": ObjectId(user_id)})


def drop_users():
    users_collection.drop()


# Usuario base
insert_user("admin@pystock.com", "1234")
