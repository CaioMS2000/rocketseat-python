from src.drivers.jwt_handler import JWTHandler
from src.drivers.password_handler import PasswordHandler
from src.models.repositories.user_repository import UserRepository
from .interfaces.login import ILogin


class Login(ILogin):
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository
        self.__password_handler = PasswordHandler()
        self.__jwt_handler = JWTHandler()

    def create(self, username: str, password: str):
        user = self._user_repository.find_by_username(username)

        if user is None:
            raise Exception("User does not exists")

        if not self.__password_handler.compare(password, user["password"]):
            raise Exception("Invalid credentials")

        token = self.__jwt_handler.create({"user_id": user["id"]})

        return self.__format_response(user["username"], token)

    def __format_response(self, username: str, token: str):
        return {"username": username, "token": token, "access": True}
