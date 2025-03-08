from pydantic import BaseModel
from typing import Optional
from bson import ObjectId
import json

class AskQuestion(BaseModel):
    question: str

class QuestionResponse(BaseModel):
    id: Optional[str] = None
    question: str
    content: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}