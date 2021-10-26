from bson.objectid import ObjectId
from flask import jsonify
from pystock.app.services.stock_service import *
from pystock.app.config import MONGO_SERVICE
import datetime

stock_movements_collection = MONGO_SERVICE.get_stock_movements()




def insert_stock_movement(cod,quantity, type_of_movement, datetime):
    """
    Inseta un movimiento de stock
    :param cod: es el codigo unico del producto
    :param quantity: es la cantidad que se agrega o saca al stock
    :param type_of_movement: es un booleano, true significa que es una entrada de stock y false una salida de stock.
    :return: json con id del producto, codigo de producto, cantidad y un bool.
    """



    response = stock_movements_collection.insert_one({"cod": cod,
                                                      "date": datetime,
                                                 "quantity": quantity,
                                                     "type": type_of_movement})
    return ({
        "id": str(response.inserted_id),
        "cod": cod,
        "date": datetime,
        "quantity": quantity,
        "type": type_of_movement
    })






def drop_collection():
    stock_movements_collection.drop()

def get_stock_movement(code):
    return stock_movements_collection.find_one({"cod": code})
