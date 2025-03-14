# pyright: reportArgumentType=warning

from typing import cast
from src.models.repositories.user_repository import UserRepository
from src.models.settings.db_connection import ConnectionType
from mysql.connector.errors import Error


class MySQLUserRepository(UserRepository):
    def __init__(self, connection: ConnectionType) -> None:
        if connection is None:
            raise Exception("Connection not established")

        self._connection = connection

    def create(self, username: str, password: str, balance: float = 0.0):
        try:
            cursor = self._connection.cursor(dictionary=True)
            sql = "INSERT INTO users (username, password, balance) VALUES (%s, %s, %s)"
            cursor.execute(sql, (username, password, balance))
            self._connection.commit()

            # Return the created user
            return self.find_by_id(cast(int, cursor.lastrowid))
        except Error as e:
            print(f"Error creating user: {e}")
            return None
        finally:
            cursor.close()

    def find_by_id(self, id: int):
        try:
            cursor = self._connection.cursor(dictionary=True)
            sql = "SELECT id, username, balance, created_at FROM users WHERE id = %s"
            cursor.execute(sql, (id,))
            return cursor.fetchone()
        except Error as e:
            print(f"Error finding user: {e}")
            return None
        finally:
            cursor.close()

    def find_by_username(self, username: str):
        try:
            cursor = self._connection.cursor(dictionary=True)
            sql = (
                "SELECT id, username, password, balance, created_at FROM users WHERE username = %s"
            )
            cursor.execute(sql, (username,))
            return cursor.fetchone()
        except Error as e:
            print(f"Error finding user: {e}")
            return None
        finally:
            cursor.close()

    def list_all(self):
        try:
            cursor = self._connection.cursor(dictionary=True)
            cursor.execute("SELECT id, username, balance, created_at FROM users")
            return cursor.fetchall()
        except Error as e:
            print(f"Error listing users: {e}")
            return []
        finally:
            cursor.close()

    def update(
        self,
        id: int,
        username: str | None = None,
        password: str | None = None,
        balance: float | None = None,
    ) -> bool:
        try:
            cursor = self._connection.cursor()
            updates = []
            values = []

            if username:
                updates.append("username = %s")
                values.append(username)
            if password:
                updates.append("password = %s")
                values.append(password)
            if balance is not None:
                updates.append("balance = %s")
                values.append(balance)

            if not updates:
                return False

            values.append(id)
            sql = f"UPDATE users SET {', '.join(updates)} WHERE id = %s"
            cursor.execute(sql, tuple(values))
            self._connection.commit()
            return True
        except Error as e:
            print(f"Error updating user: {e}")
            return False
        finally:
            cursor.close()

    def delete(self, id: int) -> bool:
        try:
            cursor = self._connection.cursor()
            sql = "DELETE FROM users WHERE id = %s"
            cursor.execute(sql, (id,))
            self._connection.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error deleting user: {e}")
            return False
        finally:
            cursor.close()

    def update_balance(self, id: int, balance: float) -> bool:
        try:
            cursor = self._connection.cursor()
            sql = "UPDATE users SET balance = %s WHERE id = %s"
            cursor.execute(sql, (balance, id))
            self._connection.commit()
            return True
        except Error as e:
            print(f"Error updating balance: {e}")
            return False
        finally:
            cursor.close()
