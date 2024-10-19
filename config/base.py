import os
from pydantic import ConfigDict


class Settings(ConfigDict):
    db_host: str | None = os.environ.get("DB_HOST")
    db_name: str | None = os.environ.get("POSTGRES_DB")
    db_user: str | None = os.environ.get("POSTGRES_USER")
    db_password: str | None = os.environ.get("POSTGRES_PASSWORD")
