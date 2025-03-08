from pydantic import BaseModel, validator
from typing import Optional
from datetime import date

CATEGORY_MAP = {"Present": "1", "Leave": "2", "Transor": "3", "VOP": "4"}
VALID_CATEGORY_IDS = set(CATEGORY_MAP.values())  # {"1", "2", "3", "4"}

class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: str
    nation_id: str
    file_code: str
    register_date: date
    promotion_date_III: Optional[date] = None
    promotion_date_II: Optional[date] = None
    promotion_date_I: Optional[date] = None
    gender: Optional[str] = None
    date_of_birth: date
    address: Optional[str] = None
    serial_number: int
    w_op: Optional[str] = None
    place_of_transfer: Optional[str] = None
    date_of_transfer: Optional[date] = None
    category_id: Optional[str] = None  # "1", "2", "3", "4" විතරක් allowed

    @validator("category_id")
    def validate_category_id(cls, v):
        if v is not None and v not in VALID_CATEGORY_IDS:
            raise ValueError("category_id must be one of '1', '2', '3', '4'")
        return v

    class Config:
        arbitrary_types_allowed = True