from flask import Blueprint, jsonify, request
from pystock.app.services.report_service import get_report
from pystock.app.config import API_KEY


report_controller = Blueprint('report_controller', __name__)


@report_controller.route('/getReport')
def report():
    """
        '/getReport', methods=["GET"]

        :response: devuelve una lista de json con codigo, nombre y cantidad.
        """
    auth = request.headers.get("X-Api-Key")
    if auth != API_KEY:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

    return jsonify(get_report()), 201
