from src.models.settings.db_connection import db_connection_handler
from src.models.repositories.mysql.user_repository import MySQLUserRepository
from src.controllers.user_register import UserRegister
from src.views.user_register_view import UserRegisterView


def user_register_composer():
    conn = db_connection_handler.get_connection()
    model = MySQLUserRepository(conn)
    controller = UserRegister(model)
    view = UserRegisterView(controller)

    return view
