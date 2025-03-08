from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str
    GORQ_API: str
    SECRET_KEY: str = "your-secret-key-here"  # Replace with a secure key
    ALGORITHM: str = "HS256"
    JWT_EXPIRATION: int = 60  # Token validity in minutes

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()