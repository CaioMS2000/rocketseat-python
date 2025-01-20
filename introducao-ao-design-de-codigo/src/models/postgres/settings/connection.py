from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = 'postgresql://postgres:rootpassword@localhost:5432/rocketseat_python'
        self.__engine = None
        self.session = None
    
    def __enter__(self): #métodos que interagem com o uso do "with"
        self.session = sessionmaker()(bind=self.__engine)

        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb): #métodos que interagem com o uso do "with"
        self.session.close()
    
    def coonnect(self):
        self.__engine = create_engine(self.__connection_string)
        return self.__engine
    
    def get_engine(self):
        return self.__engine


db_connection_handler = DBConnectionHandler()
