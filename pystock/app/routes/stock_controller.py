from flask import Blueprint, request, jsonify
from pystock.app.services.movements_service import *
from pystock.app.config import API_KEY

stock_controller = Blueprint('stock_controller', __name__)


@stock_controller.route('/setMovement', methods=["POST"])
def add_movement():
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
    amount = credentials["amount"]
    type_of_movement = credentials["type"]

    movement = set_movement(cod, amount, type_of_movement)

    return jsonify(movement), 201


@stock_controller.route('/getMovements', methods=["GET"])
def movements():
    """
        '/getMovement', methods=["GET"]
        :response:[{
                    "id":Int        //id del movimiento de stock
                    "cod":Int,      //codigo unico interno del producto
                    "date":datetime,  //datetime de cuando se ingreso el stock
                    "cantidad":Int     //cantidad a sumar o restar al stock
                  }]
        Nota: cod, es el codigo interno de la empresa que le asigna al producto.
        """
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

    return jsonify(get_all_movements()), 200
