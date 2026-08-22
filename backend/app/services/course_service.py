# course_service.py

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.models import Course

def get_course_by_id( course_id: int, db: Session) -> Course: 
    course = (db.query(Course).filter(Course.id == course_id).first())
    if course is None: 
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = "Course not found" 
        )
    return course


def get_courses(db: Session, institution_id: int | None = None) -> list[Course]: 
    query = db.query(Course) 

    if institution_id: 
        query = query.filter(
            Course.institution_id == institution_id
        )

    return query.order_by(Course.code).all()


def get_courses_for_institution(institution_id: int, db: Session)->list[Course]: 
    return(db.query(Course).filter(Course.institution_id == institution_id).order_by(Course.code).all())
