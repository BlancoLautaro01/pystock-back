from flask import Blueprint, jsonify, request
from pystock.app.services.product_service import *


product_controller = Blueprint('product_controller', __name__)


@product_controller.route('/setProduct', methods=["POST"])
def set_product():
    credentials = request.json
    cod = credentials["cod"]
    name = credentials["name"]
    price = credentials["price"]
    desc = credentials["desc"]

    if product_exist(cod):
        return "Product with the same id already exist", 400

    product = insert_product(cod, name, price, desc)

    return jsonify(product), 201


@product_controller.route('/editProduct/<product_id>', methods=["PUT"])
def edit_product(product_id):
    credentials = request.json
    cod = credentials["cod"]
    name = credentials["name"]
    price = credentials["price"]
    desc = credentials["desc"]

    product = update_product(product_id, cod, name, price, desc)

    return jsonify(product), 201


@product_controller.route('/getProducts')
def products():
    return jsonify(get_products()), 200


@product_controller.route('/deleteProduct/<product_id>', methods=["DELETE"])
def delete_a_product(product_id):
    delete_product(product_id)
    return "Deleted", 204
