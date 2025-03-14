from src.drivers.password_handler import PasswordHandler
from src.models.repositories.user_repository import UserRepository


class UserRegister:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository
        self.__password_handler = PasswordHandler()

    def registry(self, username: str, password: str):
        user = self._user_repository.find_by_username(username)

        if user:
            raise Exception("User already exists")

        user = self.__registry_new_user(username, self.__create_hash_password(password))

        return self.__format_response(user["username"])

    def __create_hash_password(self, password: str) -> str:
        return self.__password_handler.encrypt(password)

    def __registry_new_user(self, username: str, hashed_password: str):
        return self._user_repository.create(username, hashed_password)

    def __format_response(self, username: str):
        return {"username": username, "count": 1, "type": "User"}
