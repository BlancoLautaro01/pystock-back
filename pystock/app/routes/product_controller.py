from flask import Blueprint, jsonify, request
from pystock.app.services.product_service import *


product_controller = Blueprint('product_controller', __name__)


@product_controller.route('/setProduct', methods=["POST"])
def set_product():
    credentials = request.json
    code = credentials["cod"]
    name = credentials["name"]
    price = credentials["price"]
    desc = credentials["desc"]

    if product_exist(code):
        return "Product with the same id already exist", 400

    product = insert_product(code, name, price, desc)

    return jsonify(product), 201


@product_controller.route('/getProducts')
def products():
    return jsonify(get_products()), 200


@product_controller.route('/deleteProduct/<product_id>', methods=["DELETE"])
def delete_a_product(product_id):
    delete_product(product_id)
    return "Deleted", 204
