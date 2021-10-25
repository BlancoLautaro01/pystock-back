from bson.objectid import ObjectId
from flask import jsonify
from pystock.app.config import MONGO_SERVICE

products_collection = MONGO_SERVICE.get_products()


def product_exist(cod):
    result = products_collection.find_one({"cod": cod})
    return result is not None


def insert_product(cod, name, price, desc):
    response = products_collection.insert_one({"cod": cod,
                                               "name": name,
                                               "price": price,
                                               "desc": desc})
    return ({
        "id": str(response.inserted_id),
        "cod": cod,
        "name": name,
        "price": price,
        "desc": desc
    })


def update_product(_id, cod, name, price, desc):
    if cod in get_all_codes() and str(get_by_cod(cod)['_id']) != _id:
        return jsonify({"message": "ERROR: Product with the same id already exists"}), 500

    products_collection.update_one(
        {'_id': ObjectId(_id)},
        {
            "$set": {
                "cod": cod,
                "name": name,
                "price": price,
                "desc": desc
            }
        })

    return ({
        "id": _id,
        "cod": cod,
        "name": name,
        "price": price,
        "desc": desc
    })


def get_by_cod(cod):
    return products_collection.find_one({"cod": cod})


def get_products():
    products = []
    for product in products_collection.find({}):
        products.append(
            {
                "id": str(product["_id"]),
                "cod": product["cod"],
                "name": product["name"],
                "desc": product["desc"],
                "price": product["price"],
            })
    return products


def get_all_codes():
    return [product['cod'] for product in get_products()]


def delete_product(product_id):
    products_collection.delete_one({"_id": ObjectId(product_id)})


def drop_products():
    products_collection.drop()
