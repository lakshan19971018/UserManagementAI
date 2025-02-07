from pydantic import BaseModel
from datetime import datetime

class DocumentCreate(BaseModel):
    file_code : str
    file_path: str

    class Config:
       from_attributes = True

class DocumentResponse(DocumentCreate):
    id: int


    class Config:
        from_attributes = True