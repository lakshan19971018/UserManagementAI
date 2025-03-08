from pydantic import BaseModel, validator,Field
from typing import Optional
from datetime import date

CATEGORY_MAP = {"Present": "1", "Leave": "2", "Transor": "3", "VOP": "4"}
VALID_CATEGORY_IDS = set(CATEGORY_MAP.values())

class UserCreate(BaseModel):
    name: str
    email: Optional[str] = None
    nation_id: Optional[str] = None
    file_code: str
    register_date: date
    promotion_date_III: Optional[date] = None
    promotion_date_II: Optional[date] = None
    promotion_date_I: Optional[date] = None
    gender: str
    date_of_birth: date
    address: str
    serial_number: int
    w_op: str
    place_of_transfer: Optional[str] = None
    date_of_transfer: Optional[date] = None
    category_id: Optional[str] = None

    @validator("category_id")
    def validate_category_id(cls, v):
        if v is not None and v not in VALID_CATEGORY_IDS:
            raise ValueError("category_id must be one of '1', '2', '3', '4'")
        return v

class UserResponse(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: str
    email: Optional[str] = None
    nation_id: Optional[str] = None
    file_code: str
    register_date: date
    promotion_date_III: Optional[date] = None
    promotion_date_II: Optional[date] = None
    promotion_date_I: Optional[date] = None
    gender: str
    date_of_birth: date
    address: str
    serial_number: int
    w_op: str
    place_of_transfer: Optional[str] = None
    date_of_transfer: Optional[date] = None
    category_id: Optional[str] = None

    @validator("category_id")
    def validate_category_id(cls, v):
        if v is not None and v not in VALID_CATEGORY_IDS:
            raise ValueError("category_id must be one of '1', '2', '3', '4'")
        return v

    class Config:
        arbitrary_types_allowed = True