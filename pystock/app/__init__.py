from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.run(debug=True, port=4000)
