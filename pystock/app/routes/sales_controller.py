from flask import Blueprint, jsonify, request
from pystock.app.services.sales_service import *
from pystock.app.config import API_KEY

sales_controller = Blueprint('sales_controller', __name__)


@sales_controller.route('/setVenta/<client>', methods=['POST'])
def insert_a_sale(client):
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

    products = request.json

    response = insert_sale(client, products)
    return jsonify(response[0]), response[1]


@sales_controller.route('/getVentas', methods=['GET'])
def get_all_sales():
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

    response = get_sales()
    return jsonify(response[0]), response[1]