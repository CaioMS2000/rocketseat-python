from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv(override=True)


class Settings(BaseSettings):
    JWT_SECRET_KEY: str
    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    model_config = {
        "env_file": ".env",
        "case_sensitive": True,
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }

    @classmethod
    def from_env(cls) -> "Settings":
        return cls()  # pyright: ignore[reportCallIssue]


try:
    env = Settings.from_env()
except Exception as e:
    print(f"Error loading settings: {e}")

    raise SystemExit(1)

# Exportar a instância para uso em outros módulos
__all__ = ["env"]
