from flask import Blueprint, jsonify, request
from pystock.app.services.product_service import *
from pystock.app.services.stock_movements_service import *
from pystock.app.config import API_KEY


stock_and_movements = Blueprint('stock_&_movements', __name__)


@stock_and_movements.route('/setMovement', methods=["POST"])
def addMovement():
    """
        '/setMovement', methods=["POST"]
        Request:{
                    "cod":Int,      //codigo unico del producto
                    "quantity":Int,  //cantidad a agregar o sacar del stock
                    "type":bool     //True para agregar, False para sacar stock
                }

        :response:{
                    "id":Int        //id del movimiento de stock
                    "cod":Int,      //codigo unico interno del producto
                    "date":datetime,  //datetime de cuando se ingreso el stock
                    "cantidad":Int     //cantidad a sumar o restar al stock
                  }
        Nota: cod, es el codigo interno de la empresa que le asigna al producto.
        """
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401



    credentials = request.json
    cod = credentials["cod"]
    quantity = credentials["quantity"]
    type = credentials["type"]

    if not quantity.isnumeric():
        return jsonify({"message": "ERROR: Quantity field can only be numbers"}), 500

    if not product_exist(cod):
        return jsonify({"message": "ERROR: Product code not exists"}), 500

    if not stock_exists(cod):
        if not type:
            return jsonify({"message": "ERROR: The first time to add stock, the operation must be add stock not remove instead of remove stock"}), 500
        insert_stock(cod, quantity)
    else:
        update_stock(cod, quantity, type)

    movement = insert_stock_movement(cod,quantity, type, datetime.datetime.now())

    return jsonify(movement), 201