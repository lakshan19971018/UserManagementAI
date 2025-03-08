from pydantic import BaseModel, validator
from typing import Optional

CATEGORY_MAP = {"Present": "1", "Leave": "2", "Transor": "3", "VOP": "4"}

class Category(BaseModel):
    id: str  # "1", "2", "3", "4" විතරක් allowed
    name: str

    @validator("id")
    def validate_id(cls, v):
        if v not in CATEGORY_MAP.values():
            raise ValueError("id must be one of '1', '2', '3', '4'")
        return v

    @validator("name")
    def validate_name(cls, v, values):
        if "id" in values and CATEGORY_MAP.get(v) != values["id"]:
            raise ValueError(f"name '{v}' does not match id '{values['id']}'")
        return v

    class Config:
        arbitrary_types_allowed = True