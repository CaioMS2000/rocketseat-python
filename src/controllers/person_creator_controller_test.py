import pytest
from src.controllers.person_creator_controller import PersonCreatorController


class MockPeopleRepository:
    def create(self, first_name: str, last_name: str, age: int, pet_id: int):
        pass


def test_create():
    person = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "pet_id": 1,
    }
     
    controller = PersonCreatorController(MockPeopleRepository())
    response = controller.create(person)

    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person

def test_create_error():
    person = {
        "first_name": "John7",
        "last_name": "Doe/",
        "age": 30,
        "pet_id": 1,
    }
    controller = PersonCreatorController(MockPeopleRepository())

    with pytest.raises(Exception):
        controller.create(person)
