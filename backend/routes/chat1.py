from fastapi import APIRouter, Depends
from backend.auth.current_user import get_current_user
from backend.models.user_model import User
from pydantic import BaseModel
from backend.services.ai_service import get_ai_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(request: ChatRequest, current_user: User = Depends(get_current_user)):
    ai_response = get_ai_response(request.message)
    return {
        "username": current_user.username,
        "user_message": request.message,
        "ai_response": ai_response
    }
