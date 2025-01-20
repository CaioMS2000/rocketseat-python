from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
from src.models.postgres.entities.pets import Pets
from src.models.postgres.repositories.pets_repository import PetsRepository

MOCK_CONNECTION = None
MOCK_CONNECTION_NO_RESULT = None

def setup_function(): #o mesmo que o "beforeEach" dos modulos de teste JS
    # pylint: disable=global-statement
    global MOCK_CONNECTION
    MOCK_CONNECTION = MockConnection()

    # pylint: disable=global-statement
    global MOCK_CONNECTION_NO_RESULT
    MOCK_CONNECTION_NO_RESULT = MockConnectionNoResult()

class MockConnection:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(data=[
            (
                [mock.call.query(Pets)], #quert
                [
                    Pets(name="dog", type="dog"),
                    Pets(name="cat", type="cat"),
                 ], #resultado
            )
        ])
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class MockConnectionNoResult:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found
    
    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def test_list_pets():
    pets_repository = PetsRepository(MOCK_CONNECTION)
    pets = pets_repository.list()

    MOCK_CONNECTION.session.query.assert_called_once_with(Pets)
    MOCK_CONNECTION.session.all.assert_called_once()
    MOCK_CONNECTION.session.filter.assert_not_called()

    assert len(pets) == 2
    assert pets[0].name == "dog"
    assert pets[0].type == "dog"
    assert pets[1].name == "cat"
    assert pets[1].type == "cat"

def test_delete_pet():
    pets_repository = PetsRepository(MOCK_CONNECTION)
    pets_repository.delete_by_name("dog")

    MOCK_CONNECTION.session.query.assert_called_once_with(Pets)
    MOCK_CONNECTION.session.filter.assert_called_once_with(Pets.name == "dog")

def test_list_pets_no_result():
    pets_repository = PetsRepository(MOCK_CONNECTION_NO_RESULT)
    pets = pets_repository.list()

    MOCK_CONNECTION_NO_RESULT.session.query.assert_called_once_with(Pets)
    MOCK_CONNECTION_NO_RESULT.session.all.assert_not_called()
    MOCK_CONNECTION_NO_RESULT.session.filter.assert_not_called()

    assert len(pets) == 0

def test_delete_pet_error():
    pets_repository = PetsRepository(MOCK_CONNECTION_NO_RESULT)

    with pytest.raises(Exception):
        pets_repository.delete_by_name("dog")
    
    MOCK_CONNECTION_NO_RESULT.session.rollback.assert_called_once()
