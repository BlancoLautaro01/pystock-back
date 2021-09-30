from pymongo import MongoClient

mongo_uri = 'mongodb://localhost'
client = MongoClient(mongo_uri)
db = client['pystock']
users_collection = db['users']

def get_users():
    ret = []
    for user in users_collection.find():
        ret.append({"username": user["username"]})
    return ret
    
def insert_user(username, password):
    users_collection.insert_one({"username": username, "password": password})
    return {"result": "OK"}

print (get_users())