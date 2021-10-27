from flask import Blueprint, jsonify, request
from pystock.app.services.stock_service import *
from pystock.app.services.stock_movements_service import *
from pystock.app.config import API_KEY


report = Blueprint('report', __name__)


@report.route('/getInforme')
def report():
    """
        '/getInforme', methods=["GET"]

        :response: devuelve una lista de json con codigo y cantidad.
        """
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401


    return jsonify(get_all_stock()), 201