# models/category.py
from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship
from app.db.session import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    users = relationship("User", back_populates="category", lazy="select")
