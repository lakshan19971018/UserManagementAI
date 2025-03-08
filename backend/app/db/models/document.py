from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class Document(BaseModel):
    id: Optional[str] = None
    file_path: str
    file_code: Optional[str] = None  # User reference එක string (ObjectId) විදිහට

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}