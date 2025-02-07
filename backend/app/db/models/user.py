# models/user.py
from sqlalchemy import String, Integer, Date, ForeignKey, Column
from sqlalchemy.orm import relationship
from app.db.session import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    nation_id = Column(String(255), unique=True, index=True)
    file_code = Column(String(255), unique=True, index=True)
    register_date = Column(Date)
    promotion_date_III = Column(Date)
    promotion_date_II = Column(Date)
    promotion_date_I = Column(Date)
    gender = Column(String(10),nullable=True)
    date_of_birth = Column(Date)
    address = Column(String(255), nullable=True)
    Serial_number  =Column(Integer, index=True,unique=True,) 
    W_OP = Column(String(255),index=True)
    place_of_transer = Column(String(255), index=True)
    date_of_transer =  Column(Date)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="users", lazy="joined")
