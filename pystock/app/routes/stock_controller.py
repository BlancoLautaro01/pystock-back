from flask import Blueprint, request, jsonify
from pystock.app.services.movements_service import *
from pystock.app.config import API_KEY

stock_controller = Blueprint('stock_controller', __name__)


@stock_controller.route('/setMovement', methods=["POST"])
def add_movement():
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

    credentials = request.json
    cod = credentials["cod"]
    amount = credentials["amount"]
    type_of_movement = credentials["type"]

    movement = set_movement(cod, amount, type_of_movement)

    return jsonify(movement[0]), movement[1]


@stock_controller.route('/getMovements', methods=["GET"])
def movements():
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

    return jsonify(get_all_movements()), 200


@stock_controller.route('/deleteMovement/<movement_id>', methods=["DELETE"])
def delete_a_movement(movement_id):
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

    delete_movement(movement_id)
    return "Deleted", 204
