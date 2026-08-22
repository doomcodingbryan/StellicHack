# courses.py 

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.schemas import CourseResponse
from app.services.course_service import (
    get_course_by_id,
    get_courses
)

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


@router.get(
    "",
    response_model=list[CourseResponse]
)
def list_courses(
    institution_id: int | None = Query(None),
    db: Session = Depends(get_db)
):
    return get_courses(
        db,
        institution_id
    )


@router.get(
    "/{course_id}",
    response_model=CourseResponse
)
def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    return get_course_by_id(
        course_id,
        db
    )