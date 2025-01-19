from sqlalchemy.orm.exc import NoResultFound
from src.models.postgres.entities.people import People
from src.models.postgres.entities.pets import Pets

class PeopleRepository:
    def __init__(self, connection):
        self.__connection = connection
    
    def create(self, first_name: str, last_name: str, age: int, pet_id: int) -> People:
        with self.__connection as database:
            try:
                new_person = People(first_name=first_name, last_name=last_name, age=age, pet_id=pet_id)
                database.session.add(new_person)
                database.session.commit()
                database.session.refresh(new_person)

                return new_person

            except Exception as e:
                database.session.rollback()
                
                raise e
    
    def get(self, person_id: int) -> People:
        with self.__connection as database:
            try:
                person = database.session.query(People).outerjoin(Pets, Pets.id == People.pet_id).filter(People.id == person_id).with_entities(
                    People.first_name,
                    People.last_name,
                    Pets.name.label('pet_name'),
                    Pets.type.label('pet_type')
                ).one()

                return person

            except NoResultFound:
                return None
            except Exception as e:
                database.session.rollback()
                raise e
