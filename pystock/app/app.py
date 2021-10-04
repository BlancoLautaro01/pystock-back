from flask import jsonify, request
from flask import Flask
from flask_cors import CORS

from pystock.app.login_manager import *
from pystock.app.dao.user_mongo_dao import get_id, insert_user, get_password, user_exist
from pystock.app.token_manager import generate_token




app = Flask(__name__)
CORS(app)


@app.route('/test')
def test():
    return jsonify({'value': 'True'})


@app.route('/login', methods=["POST"])
def login():
    #Linea para poder probar con un usuario
    insert_user("email@pueba.com", "1234")

    credentials = request.form
    email = credentials["email"]
    password = credentials["password"]

    print("pk1@")
    print(email)
    print(password)
    print("exist " + user_exist(email))
    print(check_login(email, password))
    print(get_password(email))
    print(get_id(email))
    print("pk@2")
    """
    if check_login(email, password):
        response = {"id":get_id(email), "token" :generate_token()}
    else:
        response = {"Usuario o contraseña no validos"}
    return jsonify(response)
    """


app.run(debug=True, port=4000)
