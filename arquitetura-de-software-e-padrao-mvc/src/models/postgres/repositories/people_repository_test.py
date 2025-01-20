from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
import pytest
from sqlalchemy.orm.exc import NoResultFound
from src.models.postgres.entities.people import People
from src.models.postgres.entities.pets import Pets
from src.models.postgres.repositories.people_repository import PeopleRepository

MOCK_CONNECTION = None
MOCK_CONNECTION_NO_RESULT = None

def setup_function():
    
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
                [mock.call.query(People)], 
                [
                    People(first_name="John", last_name="Doe", age=30, pet_id=1),
                ],
            ),
            (
                [mock.call.query(Pets)], 
                [
                    Pets(id=1, name="dog", type="dog"),
                ],
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

@pytest.mark.skip()
def test_create_person():
    people_repository = PeopleRepository(MOCK_CONNECTION)
    new_person = people_repository.create("Jane", "Doe", 25, 1)

    MOCK_CONNECTION.session.add.assert_called_once()
    MOCK_CONNECTION.session.commit.assert_called_once()
    MOCK_CONNECTION.session.refresh.assert_called_once()

    assert new_person.first_name == "Jane"
    assert new_person.last_name == "Doe"
    assert new_person.age == 25
    assert new_person.pet_id == 1

@pytest.mark.skip()
def test_get_person():
    people_repository = PeopleRepository(MOCK_CONNECTION)
    person = people_repository.get(1)

    MOCK_CONNECTION.session.query.assert_called_once_with(People)
    MOCK_CONNECTION.session.outerjoin.assert_called_once_with(Pets, Pets.id == People.pet_id)
    MOCK_CONNECTION.session.filter.assert_called_once_with(People.id == 1)
    MOCK_CONNECTION.session.one.assert_called_once()

    assert person.first_name == "John"
    assert person.last_name == "Doe"
    assert person.pet_name == "dog"
    assert person.pet_type == "dog"

@pytest.mark.skip()
def test_get_person_no_result():
    people_repository = PeopleRepository(MOCK_CONNECTION_NO_RESULT)
    person = people_repository.get(1)

    MOCK_CONNECTION_NO_RESULT.session.query.assert_called_once_with(People)
    MOCK_CONNECTION_NO_RESULT.session.outerjoin.assert_called_once_with(Pets, Pets.id == People.pet_id)
    MOCK_CONNECTION_NO_RESULT.session.filter.assert_called_once_with(People.id == 1)
    MOCK_CONNECTION_NO_RESULT.session.one.assert_called_once()

    assert person is None
