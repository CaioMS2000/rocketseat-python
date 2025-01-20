from src.controllers.interfaces.pet_deleter_controller import PetDeleterControllerInterface
from src.models.postgres.interfaces.pets_repository import PetsRepositoryInterface

class PetDeleterController(PetDeleterControllerInterface):
    def __init__(self, pets_repository: PetsRepositoryInterface):
        self.__pets_repository = pets_repository
    
    def delete(self, name: str):
        self.__pets_repository.delete_by_name(name)
