from fastapi import APIRouter, HTTPException
from models.user_model import UserRegister, UserLogin
from auth.auth_handler import hash_password, verify_password, create_access_token, fake_users_db

router = APIRouter()

@router.post("/register")
def register(user: UserRegister):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed = hash_password(user.password)
    fake_users_db[user.username] = {"password": hashed}

    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin):
    db_user = fake_users_db.get(user.username)

    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}