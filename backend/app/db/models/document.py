from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base
from sqlalchemy import Column

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer,primary_key=True,index =True)
    file_path = Column(String(255), unique=True, index=True)
    file_code = Column(Integer,ForeignKey("users.id"))
    documents = relationship("Document", back_populates="user")