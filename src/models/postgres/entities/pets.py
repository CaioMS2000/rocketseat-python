from sqlalchemy import Column, Integer, String
from src.models.postgres.settings.base import Base


class Pets(Base):
    __tablename__ = 'pets'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

    def __repr__(self):
        return f'Pets [id={self.id}, name={self.name}, type={self.type}]'
