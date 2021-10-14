from flask import Blueprint, jsonify, request
from pystock.app.services.product_service import *


product_controller = Blueprint('product_controller', __name__)

@product_controller.route('/setProduct', methods=["POST"])
def set_product():
    credentials = request.json
    id_code = credentials["id_code"]
    name = credentials["name"]
    price = credentials["price"]
    description = credentials["description"]

    if product_exist(id_code):
        return "Product with the same id already exist", 500
    product = insert_product(id_code, name, price, description)
    return jsonify(product), 201