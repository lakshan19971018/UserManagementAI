from pydantic import BaseModel, validator
from typing import Optional

CATEGORY_MAP = {"Present": "1", "Leave": "2", "Transor": "3", "VOP": "4"}

class CategoryCreate(BaseModel):
    name: str

    @validator("name")
    def validate_name(cls, v):
        if v not in CATEGORY_MAP:
            raise ValueError("name must be one of 'Present', 'Leave', 'Transor', 'VOP'")
        return v

class CategoryResponse(BaseModel):
    id: str  # "1", "2", "3", "4"
    name: str

    @validator("id")
    def validate_id(cls, v):
        if v not in CATEGORY_MAP.values():
            raise ValueError("id must be one of '1', '2', '3', '4'")
        return v

    class Config:
        arbitrary_types_allowed = True