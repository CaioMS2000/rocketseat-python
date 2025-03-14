from flask import Blueprint, jsonify, request

bank_routes_bp = Blueprint("bank_routes", __name__)


@bank_routes_bp.route("/", methods=["GET"])
def get_bank_accounts():
    return jsonify({"message": "Hello, World!"})
