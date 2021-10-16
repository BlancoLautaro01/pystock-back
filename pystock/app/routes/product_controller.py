from flask import Blueprint, jsonify, request
from pystock.app.services.product_service import *


product_controller = Blueprint('product_controller', __name__)


@product_controller.route('/setProduct', methods=["POST"])
def set_product():
    credentials = request.json
    code = credentials["cod"]
    name = credentials["name"]
    price = credentials["price"]
    description = credentials["desc"]

    if product_exist(code):
        return "Product with the same id already exist", 400

    product = insert_product(code, name, price, description)

    return jsonify(product), 201
