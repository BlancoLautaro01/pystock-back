from pymongo import MongoClient

mongo_uri = 'mongodb://localhost'
client = MongoClient(mongo_uri)
db = client['pystock']
users_collection = db['users']


def user_exist(username):
    result = users_collection.find_one({"username": username})
    return result is not None


def insert_user(username, password):
    if not user_exist(username):
        users_collection.insert_one({"username": username, "password": password})



def get_credentials(username):
    return users_collection.find_one({"username": username})









# machete para mi, para mas adelante.
# delete_one para borrar
