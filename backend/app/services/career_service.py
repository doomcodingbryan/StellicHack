# career_service.py

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.models import Career, Career_Skill

def get_career_by_id(career_id: int, db: Session) -> Career: 
    career = (db.query(Career).filter(Career.id == career_id).first())
    if career is None: 
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = "Career not found" 
        )
    return career


def get_all_careers(db: Session) -> list[Career]: 
    return db.query(Career).order_by(Career.title).all()


def search_careers(db: Session, query: str | None = None) -> list[Career]: 
    careers = db.query(Career) 

    if query: 
        careers = careers.filter(
            Career.title.ilike(f"%{query}%")
        )

    return careers.order_by(Career.title).all()


def get_career_skills(career_id: int, db: Session): 
    return(db.query(Career_Skill).filter(Career_Skill.career_id == career_id).all())
