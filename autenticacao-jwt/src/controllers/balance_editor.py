from src.drivers.jwt_handler import JWTHandler
from src.drivers.password_handler import PasswordHandler
from src.models.repositories.user_repository import UserRepository


class BalanceEditor:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository
        self.__password_handler = PasswordHandler()
        self.__jwt_handler = JWTHandler()

    def edit(self, user_id: int, new_balance: float):
        self._user_repository.update_balance(user_id, new_balance)

        return {"type": "User", "count": 1, "balance": new_balance}
