from bson.objectid import ObjectId
from pystock.app.config import MONGO_SERVICE


products_collection = MONGO_SERVICE.get_products()


def product_exist(id_code):
    result = products_collection.find_one({"id_code": id_code})
    return result is not None


def insert_product(id_code, name, price, description):
    if not product_exist(id_code):
        response = products_collection.insert_one({"id_code": id_code,
                                                   "name": name,
                                                   "price": price,
                                                   "description": description})
        return({
            "id": str(response.inserted_id),
            "name": name,
            "price": price,
            "description": description
        })


def drop_products():
    products_collection.drop()


def main():

    print("Haciendo algo")

main()