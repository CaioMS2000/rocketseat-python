from typing import TypeGuard
from src.controllers.interfaces.balance_editor import IBalanceEditor
from src.views.http_types.http_request import HTTPRequest
from src.views.http_types.http_response import HTTPResponse
from src.views.view import View

class BalanceEditorView(View):
    def __init__(self, controller: IBalanceEditor) -> None:
        self._controller = controller
    
    def handler(self, request: HTTPRequest) -> HTTPResponse:
        body = request.body or {}

        if not self.__is_valid_body(body):
            raise ValueError("Invalid body")

        query_params = request.query_params or {}

        if not self.__is_valid_query_params(query_params):
            raise ValueError("Invalid params")

        new_balance = body['balance']
        user_id = query_params['user_id']
        response = self._controller.edit(int(user_id), float(new_balance))

        return HTTPResponse(body={"data": response})
    
    def __is_valid_body(self, body: object) -> TypeGuard[dict[str, str]]:
        return (
            isinstance(body, dict)
            and all(key in body for key in ['balance'])
            and isinstance(body['balance'], str)
        )
    
    def __is_valid_query_params(self, query_params: object) -> TypeGuard[dict[str, str]]:
        return (
            isinstance(query_params, dict)
            and all(key in query_params for key in ['user_id'])
            and isinstance(query_params['user_id'], str)
        )