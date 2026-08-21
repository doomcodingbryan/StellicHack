# skill_service.py

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.models import Skill

def get_skill_by_id( skill_id: int, db: Session ) -> Skill: 
    skill = (db.query(Skill).filter(Skill.id == skill_id).first())
    if skill is None: 
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = "Skill not found"
        )
    return skill