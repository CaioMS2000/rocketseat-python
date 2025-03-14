from datetime import datetime, timedelta, timezone
import jwt
import os
from dotenv import load_dotenv

load_dotenv()


class JWTHandler:
    def __init__(self) -> None:
        self.__algorithm = "HS256"
        self.__secret = os.getenv("JWT_SECRET")

        if not self.__secret:
            raise Exception("JWT_SECRET is not set")

    def create(self, body: dict = {}):
        token = jwt.encode(
            {"exp": datetime.now(timezone.utc) + timedelta(minutes=1), **body},
            self.__secret,
            algorithm=self.__algorithm,
        )

        return token

    def decode(self, token: str):
        algorithms = [].append(self.__algorithm)

        return jwt.decode(token, self.__secret, algorithms=algorithms)
