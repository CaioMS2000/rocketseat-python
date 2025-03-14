from typing import TypeAlias
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.abstracts import MySQLConnectionAbstract
import mysql.connector
from src.configs.env import env

ConnectionType: TypeAlias = PooledMySQLConnection | MySQLConnectionAbstract | None


class __DBConnectionHandler:
    def __init__(self) -> None:
        self._host = env.DB_HOST
        self._user = env.DB_USER
        self._password = env.DB_PASSWORD
        self._database = env.DB_NAME
        self._connection = None

    def connect(self):
        self._connection = mysql.connector.connect(
            host=self._host, user=self._user, password=self._password, database=self._database
        )

        return self._connection

    def disconnect(self):
        pass

    def get_connection(self) -> ConnectionType:
        return self._connection

    @property
    def cursor(self):
        if self._connection is None:
            raise Exception("Connection not established")

        return self._connection.cursor()


db_connection_handler = __DBConnectionHandler()
