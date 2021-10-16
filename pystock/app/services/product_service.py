from bson.objectid import ObjectId
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
    products_collection.update(
        {'_id': ObjectId(_id)},
        {
            "cod": cod,
            "name": name,
            "price": price,
            "desc": desc
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


def delete_product(product_id):
    products_collection.delete_one({"_id": ObjectId(product_id)})


def drop_products():
    products_collection.drop()
