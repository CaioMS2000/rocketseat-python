from src.models.settings.db_connection import db_connection_handler
from src.models.repositories.mysql.user_repository import MySQLUserRepository
from src.controllers.balance_editor import BalanceEditor
from src.views.balance_editor_view import BalanceEditorView


def balance_editor_composer():
    conn = db_connection_handler.get_connection()
    model = MySQLUserRepository(conn)
    controller = BalanceEditor(model)
    view = BalanceEditorView(controller)

    return view
