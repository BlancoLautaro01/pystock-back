from flask import Blueprint, jsonify, request

from pystock.app.utils.login_manager import check_login
from pystock.app.services.user_service import get_id, get_users, insert_user, user_exist, delete_user
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

    if not check_login(email, password):
        return "User not fond", 500

    return {"id": get_id(email), "apikey": API_KEY}


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

    if user_exist(email):
        return jsonify({"message": "ERROR: User email already exist"}), 500

    user = insert_user(email, password)
    return jsonify(user), 201


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
