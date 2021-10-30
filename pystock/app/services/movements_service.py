from bson.objectid import ObjectId
from pystock.app.config import MONGO_SERVICE
from pystock.app.services.product_service import get_by_cod, product_exist
import datetime

movement_collection = MONGO_SERVICE.get_movements()


def set_movement(cod, amount, type_of_movement):
    """
    Inseta un movimiento de stock
    :param cod: es el codigo unico del producto
    :param amount: es la cantidad que se agrega o saca al stock
    :param type_of_movement: es un booleano, true significa que es una entrada de stock y false una salida de stock.
    :return: json con id del producto, codigo de producto, cantidad y un bool.
    """

    if not isinstance(amount, int) and not amount.isnumeric():
        return {"message": "ERROR: Quantity field can only be numbers"}, 500

    amount = int(amount)

    if not product_exist(cod):
        return {"message": "ERROR: Product code not exists"}, 500

    if amount <= 0:
        return {"message": "ERROR: Amount cant be less than 1"}, 500

    if total_amount_of(cod) < amount and not type_of_movement:
        return {"message": "ERROR: Out movement cant leave a negative product stock"}, 500

    product = get_by_cod(cod)
    movement_datetime = datetime.datetime.now()

    movement = movement_collection.insert_one({"cod": cod,
                                               "name": product["name"],
                                               "date": movement_datetime,
                                               "amount": amount,
                                               "type": type_of_movement})

    return ({
        "id": str(movement.inserted_id),
        "cod": cod,
        "name": product["name"],
        "date": movement_datetime,
        "amount": amount,
        "type": type_of_movement
    }, 201)


def total_amount_of(cod):
    total_amount = 0
    for movement in get_all_movements():
        if movement["cod"] == cod:
            if movement["type"]:
                total_amount += int(movement["amount"])
            else:
                total_amount -= int(movement["amount"])

    return total_amount


def exists_movement_of(cod):
    return movement_collection.find_one({"cod": cod}) is not None


def get_all_movements():
    movements = []
    for movement in movement_collection.find({}):
        movements.append(
            {
                "id": str(movement["_id"]),
                "cod": movement["cod"],
                "name": movement["name"],
                "date": movement["date"],
                "amount": movement["amount"],
                "type": movement["type"],
            })
    return movements


def get_movement_by_cod(cod):
    return movement_collection.find_one({"cod": cod})


def get_all_movement_codes():
    return [movement['cod'] for movement in get_all_movements()]


def delete_movement(movement_id):
    movement_collection.delete_one({"_id": ObjectId(movement_id)})


def drop_collection():
    movement_collection.drop()
