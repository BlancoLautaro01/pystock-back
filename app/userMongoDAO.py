from pymongo import MongoClient


class userDAO():

    def __init__(self):
        self.mongo_uri = 'mongodb://localhost'
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client['pystock']
        self.users_collection = self.db['users']

    @property
    def user_collection(self):
        return self.users_collection

    def user_exist(self, username):
        result = self.users_collection.find_one({"username": username})
        print("here" + result["username"])
        return username == result["username"]

    def insert_user(self, username, password):
        self.users_collection.insert_one({"username": username, "password": password})
        return {"insert_user": "OK"}


def main():
    dao = userDAO
    dao.insert_user(dao, "Pk", "Secret")
    #print(userDAO.user_exist("Luis"))
main()

# machete para mi, para mas adelante.
# delete_one para borrar
