from pydantic import BaseModel

class AskQuestion(BaseModel):
    question: str

    class Config:
        from_attributes = True

class QuestionResponse(BaseModel):
    
    question: str
    content: str  # Add this to include the assistant's response
