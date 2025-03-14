from typing import TypeGuard, Any
from src.controllers.interfaces.user_register import IUserRegister
from src.views.http_types.http_request import HTTPRequest
from src.views.http_types.http_response import HTTPResponse
from src.views.view import View


class UserRegisterView(View):
    def __init__(self, controller: IUserRegister) -> None:
        self._controller = controller

    def handler(self, request: HTTPRequest) -> HTTPResponse:
        body: dict[str, Any] | None = request.body

        if not self.__is_valid_body(body):
            raise ValueError("Invalid body")

        username: str = body["username"]
        password: str = body["password"]
        response = self._controller.registry(username, password)

        return HTTPResponse(body={"data": response}, status_code=201)

    def __is_valid_body(self, body: object) -> TypeGuard[dict[str, str]]:
        return (
            isinstance(body, dict)
            and all(key in body for key in ["username", "password"])
            and isinstance(body["username"], str)
            and isinstance(body["password"], str)
        )
