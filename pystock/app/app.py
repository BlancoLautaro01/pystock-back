from flask import jsonify, request
from flask import Flask
from flask_cors import CORS

from pystock.app.login_manager import *
from pystock.app.dao.user_mongo_dao import get_id
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


app.run(debug=True, port=4000)
