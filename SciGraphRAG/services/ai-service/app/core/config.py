"""Application configuration loaded from environment variables."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime settings for the FastAPI process."""

    model_config = SettingsConfigDict(
        env_prefix="AI_SERVICE_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    name: str = "SciGraphRAG AI Service"
    version: str = "0.1.0"
    environment: str = "development"


@lru_cache
def get_settings() -> Settings:
    """Load and cache validated runtime settings."""
    return Settings()

