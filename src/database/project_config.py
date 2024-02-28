from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool
    CORS_ALLOWED_ORIGINS: str


settings = Settings()
