from fastapi import FastAPI
from backend.routes import auth
from backend.database import Base, engine

app = FastAPI(title="OpenMind AI")

# Jadval yaratish
Base.metadata.create_all(bind=engine)

# Router ulash
app.include_router(auth.router)
