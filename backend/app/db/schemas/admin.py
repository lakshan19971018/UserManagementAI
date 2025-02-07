from pydantic import BaseModel
from typing import Optional

class AdminLogin(BaseModel):
    email:str
    password:str

class AdminCreate(BaseModel):

    email:str
    password:str
    
    class Config:
        from_attributes = True
class AdminResponse(AdminCreate):
    id:int
    password:Optional[str]

class AdminTokenResponse(BaseModel):
    access_token: str
    token_type: str   