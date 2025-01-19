from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.postgres.entities.pets import Pets

class PetsRepository:
    def __init__(self, connection):
        self.__connection = connection
    
    def list(self) -> List[Pets]:
        with self.__connection as database:
            try:
                pets = database.session.query(Pets).all()

                return pets
            except NoResultFound:
                return []
    
    def delete(self, pet_id: int) -> bool:
        with self.__connection as database:
            try:
                database.session.query(Pets).filter(Pets.id == pet_id).delete()
                database.session.commit()

            except Exception as e:
                database.session.rollback()

                raise e
    
    def delete_by_name(self, name: str) -> bool:
        with self.__connection as database:
            try:
                database.session.query(Pets).filter(Pets.name == name).delete()
                database.session.commit()

            except Exception as e:
                database.session.rollback()

                raise e
