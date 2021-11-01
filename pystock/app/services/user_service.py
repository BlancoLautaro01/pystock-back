from bson.objectid import ObjectId
from pystock.app.config import MONGO_SERVICE
from pystock.app.config import API_KEY
from pystock.app.utils.login_manager import check_login


users_collection = MONGO_SERVICE.get_users()


def user_exist(email):
    result = users_collection.find_one({"email": email})
    return result is not None


def login_service(email, password):
    if not check_login(email, password):
        return {"message": "User not found"}, 500

    return {"id": get_id(email), "apikey": API_KEY}, 200


def insert_user(email, password):
    if user_exist(email):
        return {"message": "ERROR: User email already exist"}, 500

    user = users_collection.insert_one({"email": email, "password": password})

    return({
        "id": str(user.inserted_id),
        "email": email
    }, 201)


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
