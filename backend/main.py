from fastapi import FastAPI
from database import Base, engine
from routes import auth, profile, chat1, problems

app = FastAPI(title="OpenMind AI")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(chat1.router)
app.include_router(problems.router)
