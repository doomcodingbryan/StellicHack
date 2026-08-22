# projects.py 

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.dependencies import (
    get_db,
    get_current_user
)

from app.models.models import User

from app.schemas.schemas import (
    ProjectCreate,
    ProjectResponse
)

from app.services.student_service import (
    get_student_for_user
)

from app.services.project_service import (
    create_student_project,
    get_student_projects,
    get_project_by_id
)


router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.get(
    "/me",
    response_model=list[ProjectResponse]
)
def get_my_projects(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    student = get_student_for_user(
        current_user.id,
        db
    )

    return get_student_projects(
        student.id,
        db
    )


@router.post(
    "/me",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED
)
def create_my_project(
    data: ProjectCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    student = get_student_for_user(
        current_user.id,
        db
    )

    return create_student_project(
        student.id,
        data,
        db
    )


@router.get(
    "/{project_id}",
    response_model=ProjectResponse
)
def get_project(
    project_id: int,
    db: Session = Depends(get_db)
):

    return get_project_by_id(
        project_id,
        db
    )