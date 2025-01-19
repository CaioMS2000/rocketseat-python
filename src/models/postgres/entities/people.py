from sqlalchemy import Column, ForeignKey, Integer, String
from src.models.postgres.settings.base import Base


class People(Base):
    __tablename__ = 'people'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)

    def __repr__(self):
        return f'People [id={self.id}, first_name={self.first_name}, last_name={self.last_name}, age={self.age}, pet_id={self.pet_id}]'
