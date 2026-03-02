from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.models.user_model import User
from backend.auth.auth_handler import hash_password, verify_password
from backend.database import get_db
from pydantic import BaseModel

router = APIRouter()

class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Foydalanuvchi mavjud")
    new_user = User(username=user.username, password=hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Foydalanuvchi muvaffaqiyatli ro‘yxatdan o‘tdi"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Noto‘g‘ri username yoki password")
    return {"message": f"Salom, {user.username}! Login muvaffaqiyatli."}
