from flask import Flask
from src.models.settings.db_connection import db_connection_handler
from src.routes.bank_account_routes import bank_routes_bp

db_connection_handler.connect()

app = Flask(__name__)

app.register_blueprint(bank_routes_bp)