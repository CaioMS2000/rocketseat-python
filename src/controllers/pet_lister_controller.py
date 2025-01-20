from typing import Dict, List
from src.models.postgres.entities.pets import Pets
from src.models.postgres.interfaces.pets_repository import PetsRepositoryInterface


class PetListerController:
    def __init__(self, pets_repository: PetsRepositoryInterface):
        self.__pets_repository = pets_repository

    def list(self):
        pets = self.__get_pets()

        return self.__format_response(pets)

    def __get_pets(self) -> List[Pets]:
        return self.__pets_repository.list()
    
    def __format_response(self, pets: List[Pets]) -> Dict:
        formatted_pets = []

        for pet in pets:
            formatted_pets.append({
                "type": pet.type,
                "name": pet.name,
            })
        
        return {"data": {"type": "Pets", "count": len(pets), "attributes": formatted_pets}}
