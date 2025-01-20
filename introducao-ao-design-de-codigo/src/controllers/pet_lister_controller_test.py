from src.controllers.pet_lister_controller import PetListerController
from src.models.postgres.entities.pets import Pets

class MockPetsRepository:
    def list(self):
        return [
            Pets(type="Dog", name="Rex"),
            Pets(type="Cat", name="Tom"),
            Pets(type="Bird", name="Tweety"),
        ]


def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()
    expected_response = {
        "data": {
            "type": "Pets",
            "count": 3,
            "attributes": [
                {"type": "Dog", "name": "Rex"},
                {"type": "Cat", "name": "Tom"},
                {"type": "Bird", "name": "Tweety"},
            ],
        }
    }

    assert response == expected_response
