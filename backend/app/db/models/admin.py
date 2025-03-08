from pydantic import BaseModel
from typing import Optional
from bson import ObjectId
from datetime import datetime

class Admin(BaseModel):
    id: Optional[str] = None
    email: str
    hashed_password: str
    created_at: Optional[datetime] = None  # MongoDB වල manually set කරන්න

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}