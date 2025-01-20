from src.controllers.person_finder_controller import PersonFinderController

class MockPerson:
    def __init__(self, first_name: str, last_name: str, pet_name: str, pet_type: str):
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.pet_type = pet_type


class MockPeopleRepository:
    # pylint: disable=unused-argument
    def get(self, person_id: int):
        return MockPerson("John", "Doe", "Fido", "Dog")


def test_find_person():
    controller = PersonFinderController(MockPeopleRepository())
    person = controller.find(person_id=1)
    expected_response = {
        "data": {
            "type": "Person",
            "count": 1,
            "attributes": {
                "first_name": "John",
                "last_name": "Doe",
                "pet_name": "Fido",
                "pet_type": "Dog",
            },
        }
    }

    assert person == expected_response
