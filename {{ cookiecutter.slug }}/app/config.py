import os
from pathlib import Path


class BaseSettings:
    BASE_DIR = Path(__file__).resolve().parent

    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", 8080))
    DEBUG = os.getenv("DEBUG", "False")

    STATIC_URL = "/static/"
    STATIC_DIR = BASE_DIR / "static"
    TEMPLATES_DIR = BASE_DIR / "templates"


class DatabaseSettings:
    pass


class SQLiteSettings(DatabaseSettings):
    SQLITE_URI: str = "./sql_app.db"
    SQLITE_SYNC_PREFIX: str = "sqlite:///"
    SQLITE_ASYNC_PREFIX: str = "sqlite+aiosqlite:///"


class Settings(BaseSettings, SQLiteSettings):
    pass


settings = Settings()
