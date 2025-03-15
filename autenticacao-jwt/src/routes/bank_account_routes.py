from flask import Blueprint, jsonify, request
from src.composer.balance_editor_composer import balance_editor_composer
from src.composer.login_composer import login_composer
from src.views.http_types.http_request import HTTPRequest
from src.composer.user_register_composer import user_register_composer

bank_routes_bp = Blueprint("bank_routes", __name__)


@bank_routes_bp.route("/bank/registry", methods=["POST"])
def registry_user():
    req = HTTPRequest(body=request.json)
    response = user_register_composer().handler(req)

    return jsonify(response.body), response.status_code


@bank_routes_bp.route("/bank/login", methods=["POST"])
def login():
    req = HTTPRequest(body=request.json)
    response = login_composer().handler(req)

    return jsonify(response.body), response.status_code


@bank_routes_bp.route("/bank/balance/<user_id>", methods=["PATCH"])
def edit_balance(user_id):
    req = HTTPRequest(body=request.json, query_params={"user_id": user_id})
    response = balance_editor_composer().handler(req)

    return jsonify(response.body), response.status_code
