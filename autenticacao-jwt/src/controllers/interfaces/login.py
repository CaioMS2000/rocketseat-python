from abc import ABC, abstractmethod


class ILogin(ABC):
    @abstractmethod
    def create(self, username: str, passwor: str): ...
