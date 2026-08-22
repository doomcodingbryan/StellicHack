# degree_service.py

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.models import Degree

def get_degree_by_id(degree_id: int, db: Session) -> Degree: 
    degree = (db.query(Degree).filter(Degree.id == degree_id).first())
    if degree is None: 
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = "Degree not found" 
        )
    return degree

def get_degrees_for_institution(
    institution_id: int, 
    db: Session
) -> list[Degree]: 
    return (
        db.query(Degree)
        .filter(Degree.institution_id == institution_id)
        .order_by(Degree.degree_name)
        .all()
    )


def get_all_degrees(db: Session) -> list[Degree]:
    return(db.query(Degree).order_by(Degree.degree_name).all())

