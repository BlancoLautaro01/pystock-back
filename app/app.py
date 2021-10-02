from flask import Flask, jsonify, request
from flask_cors import CORS
from connection import get_users, insert_user
from login_manager import *

app = Flask(__name__)
CORS(app)


@app.route('/test')
def test():
    return jsonify({'value': 'True'})


@app.route('/users')
def users():
    return jsonify(get_users())


@app.route('/users', methods=["POST"])
def create_user():
    return jsonify(insert_user(request.form["username"], request.form["password"]))


@app.route('/login', methods=["POST"])
def login():
     #retorno de la funcion
    response = None

    credentials = request.form
    email = credentials["email"]
    password = credentials["password"]
    checked = check_login(email, password)
    if checked:
        response = {"id", "token"}
    else:
        response = {}
    return response


if __name__ == '__main__':
    app.run(debug=True, port=4000)
