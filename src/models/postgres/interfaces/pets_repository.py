from abc import ABC, abstractmethod
from typing import List

from src.models.postgres.entities.pets import Pets

class PetsRepositoryInterface(ABC):
    @abstractmethod
    def list(self) -> List[Pets]:
        pass

    @abstractmethod
    def delete(self, pet_id: int) -> bool:
        pass

    @abstractmethod
    def delete_by_name(self, name: str) -> bool:
        pass