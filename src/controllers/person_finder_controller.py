from typing import Dict
from src.models.postgres.entities.people import People
from src.models.postgres.interfaces.people_repository import PeopleRepositoryInterface


class PersonFinderController:
    def __init__(self, people_repository: PeopleRepositoryInterface):
        self.__people_repository = people_repository
    
    def find(self, person_id: int) -> Dict:
        person = self.__find_person(person_id=person_id)

        return self.__format_response(person)
    
    def __format_response(self, person: People) -> Dict:
        return {"data": {"type": "Person", "count": 1, "attributes": {
            "first_name": person.first_name,
            "last_name": person.last_name,
            "pet_name": person.pet_name,
            "pet_type": person.pet_type,
        }}}
    
    def __find_person(self, person_id: int) -> People:
        person = self.__people_repository.get(person_id=person_id)

        if not person:
            raise Exception("Person not found")

        return person
