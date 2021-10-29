from flask import Blueprint, jsonify, request
from pystock.app.services.product_service import *
from pystock.app.config import API_KEY


product_controller = Blueprint('product_controller', __name__)


@product_controller.route('/setProduct', methods=["POST"])
def set_product():
    """
        '/setProduct', methods=["POST"]
        Request:{
                    "cod":Int,      //codigo unico del producto
                    "name":String,  //nombre del producto
                    "price":Int     //precio unitario del producto
                    "desc":String   //descripcion del producto
                }

        :response:{
                    "id":Int        //id del producto
                    "cod":Int,      //codigo unico interno del producto
                    "name":String,  //nombre del producto
                    "price":Int     //precio unitario del producto
                    "desc":String   //descripcion del producto
                  }
        Nota: cod, es el codigo interno de la empresa que le asigna al producto.
        """
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

    credentials = request.json
    cod = credentials["cod"]
    name = credentials["name"]
    price = credentials["price"]
    desc = credentials["desc"]

    if not isinstance(price, int) and not price.isnumeric():
        return jsonify({"message": "ERROR: Price field can only be numbers"}), 500

    if product_exist(cod):
        return jsonify({"message": "ERROR: Product with the same id already exists"}), 500

    product = insert_product(cod, name, price, desc)

    return jsonify(product), 201


@product_controller.route('/editProduct/<product_id>', methods=["PUT"])
def edit_product(product_id):
    """
        '/editProduct/<product_id>', methods=["PUT"]
        Request:{
                    "cod":Int,      //codigo unico del producto
                    "name":String,  //nombre del producto
                    "price":Int     //precio unitario del producto
                    "desc":String   //descripcion del producto
                }

        :response:{
                    "id":Int        //id del producto
                    "cod":Int,      //codigo unico interno del producto
                    "name":String,  //nombre del producto
                    "price":Int     //precio unitario del producto
                    "desc":String   //descripcion del producto
                  }
        """
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

    credentials = request.json
    cod = credentials["cod"]
    name = credentials["name"]
    price = credentials["price"]
    desc = credentials["desc"]

    if not price.isnumeric():
        return jsonify({"message": "ERROR: Price field can only be numbers"}), 500

    product = update_product(product_id, cod, name, price, desc)

    return jsonify(product), 201


@product_controller.route('/getProducts')
def products():
    """
        '/getProducts' metodo tipo GET
        Retorna un json con todos los productos.
        """
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

    return jsonify(get_products()), 200


@product_controller.route('/deleteProduct/<product_id>', methods=["DELETE"])
def delete_a_product(product_id):
    """
        '/deleteProduct/<product_id>', methods=["DELETE"]
        Borra un producto con id: <product_id>'
        Retorna "Deleted" con codigo HTPP 204
        """
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

    delete_product(product_id)
    return "Deleted", 204
