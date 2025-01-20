from abc import ABC, abstractmethod

from src.models.postgres.entities.people import People

class PeopleRepositoryInterface(ABC):
    @abstractmethod
    def create(self, first_name: str, last_name: str, age: int, pet_id: int) -> People:
        pass

    @abstractmethod
    def get(self, person_id: int) -> People:
        pass
