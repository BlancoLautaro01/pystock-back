from pystock.app.config import MONGO_SERVICE
from pystock.app.services.product_service import *

stock_collection = MONGO_SERVICE.get_stock()


def insert_stock(cod, quantity):

    name = get_by_cod(cod)["name"]

    response = stock_collection.insert_one({"cod": cod,
                                            "name": name,
                                            "quantity": quantity
                                            })
    return ({
        "id": str(response.inserted_id),
        "cod": cod,
        "name": name,
        "quantity": quantity,
    })


def update_stock(cod, quantity, type_of_movement):
    """
    Se encarga de mantener actualizado la cantidad del stock
    si type_of_movement es True agrega stock en una cantidad igual a quantity
    y en caso de False lo resta
    """
    stock = stock_collection.find_one({"cod": cod})

    if type_of_movement:
        stock["quantity"] += quantity
    else:
        stock["quantity"] -= quantity

    stock_collection.update_one(
        {'cod': cod},
        {
            "$set": {
                "quantity": stock["quantity"],
            }
        })

    return ({
        "cod": cod,
        "name": stock["name"],
        "quantity": quantity
    })


def get_stock(code):
    return stock_collection.find_one({"cod": code})

def stock_exists(code):
    return stock_collection.find_one({"cod": code}) is not None

def get_all_stock():
    return stock_collection.find()


#funciones para testing
def drop_collection():
    stock_collection.drop()

