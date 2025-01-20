from src.models.postgres.interfaces.people_repository import PeopleRepositoryInterface

class PersonCreatorController:
    def __init__(self, people_repository: PeopleRepositoryInterface):
        self.__people_repository = people_repository
