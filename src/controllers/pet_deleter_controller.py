from src.models.postgres.interfaces.pets_repository import PetsRepositoryInterface

class PetDeleterController:
    def __init__(self, pets_repository: PetsRepositoryInterface):
        self.__pets_repository = pets_repository
    
    def delete(self, name: str):
        self.__pets_repository.delete_by_name(name)
