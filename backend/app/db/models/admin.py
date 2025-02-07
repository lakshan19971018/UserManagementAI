from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer,primary_key=True,index=True)
    email  = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False,server_default=func.now())