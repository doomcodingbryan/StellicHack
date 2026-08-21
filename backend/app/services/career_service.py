# career_service.py

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.models import Career

def get_career_by_id(career_id: int, db: Session) -> Career: 
    career = (db.query(Career).filter(Career.id == career_id).first())
    if career is None: 
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = "Career not found" 
        )
    return career

