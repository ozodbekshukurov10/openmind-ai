# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers import qilish
from routes import auth, chat

# FastAPI app yaratish
app = FastAPI(
    title="OpenMind AI Backend",
    description="OpenMind AI loyihasi uchun FastAPI backend",
    version="1.0.0"
)

# CORS sozlamalari (frontend bilan ishlash uchun)
origins = [
    "http://localhost",
    "http://localhost:3000",  # agar frontend React yoki boshqa framework bo'lsa
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers ulash
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

# Test endpoint
@app.get("/")
async def root():
    return {"message": "Hello, OpenMind AI!"}