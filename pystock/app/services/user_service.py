from bson.objectid import ObjectId
from pystock.app.config import MONGO_SERVICE


users_collection = MONGO_SERVICE.get_users()


def user_exist(email):
    result = users_collection.find_one({"email": email})
    return result is not None


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


# Funciones para tests.
def delete_user_by_email(email):
    users_collection.delete_one({"email": email})


def get_password(email):
    return users_collection.find_one({"email": email})["password"]


def get_id(email):
    return str(users_collection.find_one({"email": email})["_id"])


def drop_users():
    users_collection.drop()
