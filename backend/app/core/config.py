import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# Database Configuration

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
GORQ_API  = os.getenv("GORQ_API")
DATABASE_URL = f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"

class Settings:
    SECRET_KEY: str = "your-secret-key"  # Replace with a strong secret key
    ALGORITHM: str = "HS256"
    JWT_EXPIRATION: int = 60  # Token validity in minutes

settings = Settings()
