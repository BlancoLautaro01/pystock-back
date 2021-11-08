from flask import Flask
from flask_cors import CORS

from pystock.app.routes.user_controller import user_controller
from pystock.app.routes.product_controller import product_controller
from pystock.app.routes.stock_controller import stock_controller
from pystock.app.routes.report_controller import report_controller


# App creation + Cors
app = Flask(__name__)


# Routes register
app.register_blueprint(user_controller)
app.register_blueprint(product_controller)
app.register_blueprint(stock_controller)
app.register_blueprint(report_controller)

CORS(app)

app.run(port=4000)
