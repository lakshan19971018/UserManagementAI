from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class AdminLogin(BaseModel):
    email: str
    password: str

class AdminCreate(BaseModel):
    email: str
    password: str

class AdminResponse(BaseModel):
    id: Optional[str] = None  # MongoDB '_id' string එකක් විදිහට
    email: str
    password: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class AdminTokenResponse(BaseModel):
    access_token: str
    token_type: str