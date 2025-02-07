from app.services.chat_service import asking_question
from fastapi import APIRouter, HTTPException
from app.db.schemas.chat import AskQuestion, QuestionResponse

router = APIRouter()
@router.post("/ask", response_model=QuestionResponse)
async def ask_question_endpoint(question: AskQuestion):
    try:
        # Call the service function to get the answer
        answer = str(asking_question(question=question.question))
        
        # Return the response as per the QuestionResponse model
        return {"question": question.question,  "content": answer}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
