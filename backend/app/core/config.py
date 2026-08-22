# config.py
# validate and organize the environment variables, etc. 
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Database
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: int = 5432

    DATABASE_URL: str

    BACKEND_PORT: int = 8080

    JWT_SECRET: str

    model_config = SettingsConfigDict(
        env_file = ".env", 
        env_file_encoding = "utf-8", 
        extra = "ignore"
    )

# make an instance so that we can import it somewhere else: from config import settings, settings.DATABASE_URL...
settings = Settings()