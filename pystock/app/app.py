from flask import Flask
from flask_cors import CORS

from pystock.app.routes.user_controller import user_controller

# App creation + Cors
app = Flask(__name__)
CORS(app)

# Routes register
app.register_blueprint(user_controller)

app.run(port=4000)
