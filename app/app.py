from flask import Flask, jsonify,request
from flask_cors import CORS
from connection import get_users, insert_user

app = Flask(__name__)
CORS(app)


@app.route('/test')
def test():
    return jsonify({'value': 'True'})

@app.route('/users')
def users():
    return jsonify(get_users())

@app.route('/users',methods = ["POST"])
def create_user():
    return jsonify(insert_user(request.form["username"], request.form["password"]))

if __name__ == '__main__':
    app.run(debug=True, port=4000)
