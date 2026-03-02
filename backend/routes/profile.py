from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.auth.current_user import get_current_user
from backend.database import get_db
from backend.models.user_model import User
from backend.auth.auth_handler import hash_password

router = APIRouter()

# Profilni ko‘rish
@router.get("/profile")
def read_profile(current_user: User = Depends(get_current_user)):
    return {"username": current_user.username, "message": "Bu sizning profilingiz"}

# Profilni yangilash
@router.put("/profile")
def update_profile(new_username: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    current_user.username = new_username
    db.commit()
    db.refresh(current_user)
    return {"message": "Profil yangilandi", "username": current_user.username}

# Parolni o‘zgartirish
@router.patch("/profile/password")
def change_password(new_password: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    current_user.password = hash_password(new_password)
    db.commit()
    return {"message": "Parol muvaffaqiyatli o‘zgartirildi"}

# Foydalanuvchini o‘chirish
@router.delete("/profile")
def delete_profile(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db.delete(current_user)
    db.commit()
    return {"message": "Foydalanuvchi o‘chirildi"}
