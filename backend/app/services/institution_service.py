# institution_service.py

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.models import Institution

def get_institution_by_id(institution_id: int, db: Session) -> Institution: 
    institution = (db.query(Institution).filter(Institution.id == institution_id).first())
    if institution is None: 
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = "Institution not found" 
        )
    return institution