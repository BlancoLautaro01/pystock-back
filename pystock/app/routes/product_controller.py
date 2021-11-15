from flask import Blueprint, request, jsonify
from pystock.app.services.product_service import *
from pystock.app.config import API_KEY


product_controller = Blueprint('product_controller', __name__)


@product_controller.route('/setProduct', methods=["POST"])
def set_product():
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

    credentials = request.json
    cod = credentials["cod"]
    name = credentials["name"]
    price = credentials["price"]
    desc = credentials["desc"]

    product = insert_product(cod, name, price, desc)

    return jsonify(product[0]), product[1]


@product_controller.route('/editProduct/<product_id>', methods=["PUT"])
def edit_product(product_id):
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

    credentials = request.json
    cod = credentials["cod"]
    name = credentials["name"]
    price = credentials["price"]
    desc = credentials["desc"]

    product = update_product(product_id, cod, name, price, desc)

    return jsonify(product[0]), product[1]


@product_controller.route('/getProducts')
def products():
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

    return jsonify(get_products()), 200


@product_controller.route('/deleteProduct/<product_id>', methods=["DELETE"])
def delete_a_product(product_id):
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

    delete_product(product_id)
    return "Deleted", 204


@product_controller.route('/getProductsWithStock')
def products_with_stock():
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

    return jsonify(get_products_with_stock()), 200
