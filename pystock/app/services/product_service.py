from bson.objectid import ObjectId
from pystock.app.config import MONGO_SERVICE


products_collection = MONGO_SERVICE.get_products()


def product_exist(cod):
    result = products_collection.find_one({"cod": cod})
    return result is not None


def insert_product(cod, name, price, description):
    if not product_exist(cod):
        response = products_collection.insert_one({"cod": cod,
                                                   "name": name,
                                                   "price": price,
                                                   "description": description})
        return({
            "id": str(response.inserted_id),
            "cod": cod,
            "name": name,
            "price": price,
            "description": description
        })


def drop_products():
    products_collection.drop()
