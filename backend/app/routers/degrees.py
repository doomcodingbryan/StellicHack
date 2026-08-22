# degrees.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.schemas import DegreeResponse
from app.services.degree_service import (
    get_degree_by_id,
    get_degrees_for_institution
)

router = APIRouter(
    prefix="/degrees",
    tags=["Degrees"]
)


@router.get(
    "/institution/{institution_id}",
    response_model=list[DegreeResponse]
)
def list_degrees_for_institution(
    institution_id: int,
    db: Session = Depends(get_db)
):
    return get_degrees_for_institution(
        institution_id,
        db
    )


@router.get(
    "/{degree_id}",
    response_model=DegreeResponse
)
def get_degree(
    degree_id: int,
    db: Session = Depends(get_db)
):
    return get_degree_by_id(
        degree_id,
        db
    )