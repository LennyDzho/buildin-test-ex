from pathlib import Path
from typing import Optional

from environs import Env
from pydantic import BaseModel


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

class AppConfig(BaseModel):
    """
    Application-level configuration.

    Attributes:
        debug (bool): Indicates whether debug mode is enabled.
    """
    debug: bool
    api_key: str

class DatabaseConfig(BaseModel):
    """
    Database connection configuration.

    Attributes:
        database (str): The name of the PostgreSQL database.
        user (str): The database username.
        password (str): The database password.
        host (str): The database host address.
        port (int): The port number for the database connection.
    """
    database: str
    user: str
    password: str
    host: str
    port: int

    def connection_url(self) -> str:
        """
        Build the full asynchronous PostgreSQL connection URL.

        Returns:
            str: A formatted database connection string suitable
            for SQLAlchemy with asyncpg.
        """
        return (
            f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:"
            f"{self.port}/{self.database}"
        )


class Settings(BaseModel):
    """
    Global application settings.

    Combines application and database configurations into a single model.

    Attributes:
        app (AppConfig): General application configuration.
        db (DatabaseConfig): Database connection configuration.
    """
    app: AppConfig
    db: DatabaseConfig


def load_settings() -> Settings:
    """
    Load application settings from a .env file.

    Reads environment variables from the .env file located in BASE_DIR
    and constructs a Settings instance with nested AppConfig and
    DatabaseConfig objects.

    Returns:
        Settings: Fully populated application settings.
    """
    env_path = BASE_DIR / ".env"
    env = Env()

    env.read_env(env_path)

    return Settings(
        app=AppConfig(
            debug=env.bool("DEBUG"),
            api_key=env.str("API_KEY"),
        ),
        db=DatabaseConfig(
            database=env.str("DB_NAME"),
            user=env.str("DB_USER"),
            password=env.str("DB_PASSWORD"),
            host=env.str("DB_HOST"),
            port=env.int("DB_PORT"),
        ),
    )


settings: Settings = load_settings()
"""Settings: Global instance containing loaded configuration values."""
