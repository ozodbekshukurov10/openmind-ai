from fastapi import APIRouter, Depends
from backend.auth.current_user import get_current_user
from backend.models.user_model import User
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(request: ChatRequest, current_user: User = Depends(get_current_user)):
    user_message = request.message
    ai_response = f"AI javobi: '{user_message}' matnini qabul qildim va tahlil qildim."
    return {
        "username": current_user.username,
        "user_message": user_message,
        "ai_response": ai_response
    }
