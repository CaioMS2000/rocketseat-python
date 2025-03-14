from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def create(self, username: str, password: str, balance: float = 0.0) -> dict: ...

    @abstractmethod
    def find_by_id(self, id: int) -> dict | None: ...

    @abstractmethod
    def find_by_username(self, username: str) -> dict | None: ...

    @abstractmethod
    def list_all(self) -> list[dict]: ...

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
