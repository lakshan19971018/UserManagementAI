from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class DocumentCreate(BaseModel):
    file_code: str
    file_path: str

class DocumentResponse(BaseModel):
    id: Optional[str] = None  # MongoDB '_id' string එකක් විදිහට
    file_code: str
    file_path: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}