
from pydantic import BaseModel
from typing import Optional
class CategoryCreate(BaseModel):
    name: str

    class Config:
        from_attributes = True

class CategoryResponse(CategoryCreate):
    id: int  # Make sure this matches the return fields
    name: Optional[str]

    class Config:
        from_attributes = True
