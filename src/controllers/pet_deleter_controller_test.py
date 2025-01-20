from src.controllers.pet_deleter_controller import PetDeleterController
from src.models.postgres.interfaces.pets_repository import PetsRepositoryInterface


def test_delete(mocker):
    mock_respository = mocker.Mock(spec=PetsRepositoryInterface)
    controller = PetDeleterController(mock_respository)

    controller.delete("dog")

    mock_respository.delete_by_name.assert_called_once_with("dog")
