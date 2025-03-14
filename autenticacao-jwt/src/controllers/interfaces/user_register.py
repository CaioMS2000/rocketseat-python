from abc import ABC, abstractmethod


class IUserRegister(ABC):
    @abstractmethod
    def registry(self, username: str, password: str): ...
