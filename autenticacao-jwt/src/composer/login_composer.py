from src.models.settings.db_connection import db_connection_handler
from src.models.repositories.mysql.user_repository import MySQLUserRepository
from src.controllers.login import Login
from src.views.login_view import LoginView


def login_composer():
    conn = db_connection_handler.get_connection()
    model = MySQLUserRepository(conn)
    controller = Login(model)
    view = LoginView(controller)

    return view
