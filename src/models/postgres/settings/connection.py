from sqlalchemy import create_engine

class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = 'postgresql://postgres:rootpassword@localhost:5432/rocketseat_python'
        self.__engine = None
    
    def coonnect(self):
        self.__engine = create_engine(self.__connection_string)
        return self.__engine
    
    def get_engine(self):
        return self.__engine


db_connection_handler = DBConnectionHandler()
