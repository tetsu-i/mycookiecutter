import os
from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

MODULE_DIR = Path(__file__).parent.absolute()


class _Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file_encoding="utf-8", extra="ignore")

    environment: Literal["local", "development", "stating", "production", "test"] = (
        "local"
    )


@lru_cache
def get_settings() -> _Settings:
    env = os.environ.get("ENVIRONMENT", "local")

    env_file = (MODULE_DIR / f".env.{env}",)

    return _Settings(_env_file=env_file, environment=env)


SETTINGS = get_settings()
