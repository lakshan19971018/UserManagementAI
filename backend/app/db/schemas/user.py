# schemas/user.py
from pydantic import BaseModel
from datetime import date
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: Optional[str]
    nation_id: Optional[str]
    file_code: str
    register_date :date
    promotion_date_III : Optional[date]
    promotion_date_II : Optional[date]
    promotion_date_I : Optional[date]
    gender :str
    date_of_birth : date
    address : str
    Serial_number  :int
    W_OP : str
    place_of_transer : Optional[str]
    date_of_transer :  Optional[date]
    category_id: int

    

    class Config:
        from_attributes = True

class UserResponse(UserCreate):
    id: int
