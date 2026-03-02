from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models.problem_model import Problem
from backend.auth.current_user import get_current_user, get_current_admin
from backend.models.user_model import User
from backend.services.ai_service import get_ai_solution
from pydantic import BaseModel

router = APIRouter()

class ProblemCreate(BaseModel):
    title: str
    description: str
    category: str

# Muammo qo‘shish
@router.post("/problems")
def create_problem(problem: ProblemCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_problem = Problem(
        title=problem.title,
        description=problem.description,
        category=problem.category
    )
    db.add(new_problem)
    db.commit()
    db.refresh(new_problem)

    # AI yechim taklifi
    ai_solution = get_ai_solution(problem.title, problem.description)

    return {
        "message": "Muammo qo‘shildi",
        "problem": {
            "id": new_problem.id,
            "title": new_problem.title,
            "description": new_problem.description,
            "category": new_problem.category
        },
        "ai_solution": ai_solution
    }

# Muammo o‘chirish (faqat admin)
@router.delete("/problems/{problem_id}")
def delete_problem(problem_id: int, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    problem = db.query(Problem).filter(Problem.id == problem_id).first()
    if not problem:
        raise HTTPException(status_code=404, detail="Muammo topilmadi")
    db.delete(problem)
    db.commit()
    return {"message": "Muammo admin tomonidan o‘chirildi"}
