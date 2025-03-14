from src.models.repositories.user_repository import UserRepository


class UserRegister:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository
