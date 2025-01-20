import re
from typing import Dict
from src.models.postgres.interfaces.people_repository import PeopleRepositoryInterface


class PersonCreatorController:
    def __init__(self, people_repository: PeopleRepositoryInterface):
        self.__people_repository = people_repository

    def create(self, info: Dict) -> Dict:
        first_name = info["first_name"]
        last_name = info["last_name"]
        age = info["age"]
        pet_id = info["pet_id"]

        self.__validate_name(first_name=first_name, last_name=last_name)
        self.__insert_person(
            first_name=first_name, last_name=last_name, age=age, pet_id=pet_id
        )

        return self.__format_response(info)

    def __validate_name(self, first_name: str, last_name: str) -> bool:
        non_valid_characters = re.compile(r"[^a-zA-Z]")

        if non_valid_characters.search(first_name) or non_valid_characters.search(
            last_name
        ):
            raise Exception("Invalid name")

    def __insert_person(self, first_name: str, last_name: str, age: int, pet_id: int):
        return self.__people_repository.create(
            first_name=first_name, last_name=last_name, age=age, pet_id=pet_id
        )

    def __format_response(self, info: Dict) -> Dict:
        return {"data": {"type": "Person", "count": 1, "attributes": info}}
