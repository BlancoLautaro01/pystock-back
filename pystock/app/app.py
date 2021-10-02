from flask import jsonify, request
from pystock.app.login_manager import *

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/test')
def test():
    return jsonify({'value': 'True'})


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


app.run(debug=True, port=4000)
