from fastapi import FastAPI
from backend.routes import auth, profile, chat1
from backend.database import Base, engine

app = FastAPI(title="OpenMind AI")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(chat1.router)   # chat1.py ni ulash
