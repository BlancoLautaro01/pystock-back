from flask import jsonify, request
from flask import Flask
from flask_cors import CORS

from pystock.app.login_manager import *
from pystock.app.dao.user_mongo_dao import get_id, get_users, insert_user, user_exist
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


@app.route('/users')
def users():
    return jsonify(get_users())


@app.route('/create_user', methods=["POST"])
def create_user():

    credentials = request.form
    email = credentials["email"]
    password = credentials["password"]

    if user_exist(email):
        return "User allready exist", 500
    insert_user(email, password)
    return "New user was created with email: " + email, 200


app.run(debug=True, port=4000)
