from fastapi import FastAPI
from routes.chat import router as chat_router
from routes.auth import router as auth_router

app = FastAPI(title="OpenMind AI")

app.include_router(chat_router)
app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "OpenMind AI Professional Backend 🚀"}