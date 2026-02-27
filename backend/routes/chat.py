from fastapi import APIRouter
from models.chat_model import ChatRequest, ChatResponse
from services.ai_service import generate_response

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    ai_reply = generate_response(request.message)
    return ChatResponse(response=ai_reply)
