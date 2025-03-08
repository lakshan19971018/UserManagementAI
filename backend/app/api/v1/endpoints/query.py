from app.services.chat_service import asking_question
from fastapi import APIRouter, HTTPException
from app.db.schemas.chat import AskQuestion, QuestionResponse
import json


router = APIRouter()

@router.post("/ask", response_model=QuestionResponse)
async def ask_question_endpoint(question: AskQuestion):
    try:
        result = await asking_question(question=question.question)
        content = json.dumps(result["value"])  # List → JSON string
        return {"question": question.question, "content": content}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))