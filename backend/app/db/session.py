from  sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL

# Create SQLAlchemy engine using the DATABASE_URL from config
engine = create_engine(DATABASE_URL, connect_args={"charset": "utf8mb4"})

# Create a session maker to generate sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base class for all models to inherit from
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
