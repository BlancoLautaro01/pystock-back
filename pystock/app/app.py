from flask import jsonify, request
from flask import Flask
from flask_cors import CORS

from pystock.app.login_manager import *
from pystock.app.dao.user_mongo_dao import get_id, get_users, insert_user, user_exist, delete_user
from pystock.app.token_manager import generate_token

app = Flask(__name__)
CORS(app)


@app.route('/test')
def test():
    return jsonify({'value': 'True'})


@app.route('/login', methods=["POST"])
def login():
    credentials = request.json
    email = credentials["email"]
    password = credentials["password"]

    if not check_login(email, password):
        return "User not fond", 500

    return {"id": get_id(email), "token": generate_token()}


@app.route('/getUsers')
def users():
    return jsonify(get_users()), 200


@app.route('/setUser', methods=["POST"])
def create_user():
    credentials = request.json
    email = credentials["email"]
    password = credentials["password"]

    if user_exist(email):
        return "User already exist", 500
    user = insert_user(email, password)
    return jsonify(user), 201


@app.route('/deleteUser/<user_id>', methods=["DELETE"])
def delete_a_user(user_id):
    delete_user(user_id)
    return "Deleted", 204


app.run(debug=True, port=4000)
