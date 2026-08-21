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