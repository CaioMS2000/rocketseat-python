from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def create(self, username: str, password: str, balance: float = 0.0): ...

    @abstractmethod
    def find_by_id(self, id: int): ...

    @abstractmethod
    def find_by_username(self, username: str): ...

    @abstractmethod
    def list_all(self): ...

    @abstractmethod
    def update(
        self,
        id: int,
        username: str | None = None,
        password: str | None = None,
        balance: float | None = None,
    ) -> bool: ...

    @abstractmethod
    def delete(self, id: int) -> bool: ...

    @abstractmethod
    def update_balance(self, id: int, balance: float) -> bool: ...
