# students.py

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.dependencies import (
    get_db,
    get_current_user
)

from app.models.models import User, Student_Skill
from app.schemas.schemas import (
    StudentCreate,
    StudentResponse,
    StudentCourseCreate,
    StudentCourseResponse,
    StudentSkillCreate,
    StudentSkillResponse
)

from app.services.project_service import create_student_project

from app.services.student_service import (
    get_student_for_user,
    create_student_profile
)

from app.models.models import (
    User,
    Student_Course
)
from app.services.project_service import create_student_project


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post(
    "/me",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_my_student_profile(
    data: StudentCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return create_student_profile(
        current_user.id,
        data,
        db
    )


@router.get(
    "/me",
    response_model=StudentResponse
)
def get_my_student_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return get_student_for_user(
        current_user.id,
        db
    )

@router.post(
    "/me/courses",
    response_model=StudentCourseResponse,
    status_code=status.HTTP_201_CREATED
)
def add_my_course(
    data: StudentCourseCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    student = get_student_for_user(
        current_user.id,
        db
    )

    enrollment = Student_Course(
        student_id=student.id,
        course_id=data.course_id,
        semester=data.semester,
        year=data.year,
        grade=data.grade,
        status=data.status
    )

    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)

    return enrollment


@router.post(
    "/me/skills",
    response_model=StudentSkillResponse,
    status_code=status.HTTP_201_CREATED
)
def add_my_skill(
    data: StudentSkillCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    student = get_student_for_user(
        current_user.id,
        db
    )

    skill = Student_Skill(
        student_id=student.id,
        skill_id=data.skill_id,
        proficiency=data.proficiency
    )

    db.add(skill)
    db.commit()
    db.refresh(skill)

    return skill

