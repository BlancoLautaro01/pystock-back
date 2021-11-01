from flask import Blueprint, jsonify, request

from pystock.app.services.user_service import get_id, get_users, insert_user, user_exist, delete_user, login_service
from pystock.app.config import API_KEY


user_controller = Blueprint('user_controller', __name__)


@user_controller.route('/login', methods=["POST"])
def login():
    """
    "/login"  metodo tipo POST
    Request:{
                "email":String,
                "password":String
            }

    :response:{
                    "id": Int
                    "token": String
              }
    Nota: el id es el del usuario.
    """
    credentials = request.json
    email = credentials["email"]
    password = credentials["password"]

    response = login_service(email, password)

    return jsonify(response[0]), response[1]


@user_controller.route('/getUsers')
def users():
    """
       "/getUsers"  metodo tipo GET
       :return: json con elementos usuario, cada usurio tiene un id y un email.
       """
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

    return jsonify(get_users()), 200


@user_controller.route('/setUser', methods=["POST"])
def create_user():
    """
        "/setUser"  metodo tipo POST
        Request:{
                    "email":String,
                    "password":String
                }

        :response:{
                        "id": Int
                        "email": String
                  }
        """
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

    credentials = request.json
    email = credentials["email"]
    password = credentials["password"]

    user = insert_user(email, password)
    return jsonify(user[0]), user[1]


@user_controller.route('/deleteUser/<user_id>', methods=["DELETE"])
def delete_a_user(user_id):
    """
        '/deleteUser/<user_id>' metodo tipo DELETE
        :param user_id: representa el id del usuario
        :return: "Deleted", 204
        """
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

    delete_user(user_id)
    return "Deleted", 204
