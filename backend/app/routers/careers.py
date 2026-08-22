# careers.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.schemas import CareerResponse
from app.services.career_service import (
    get_career_by_id,
    get_all_careers,
    search_careers
)

router = APIRouter(
    prefix="/careers",
    tags=["Careers"]
)


@router.get(
    "",
    response_model=list[CareerResponse]
)
def list_careers(
    q: str | None = Query(None),
    db: Session = Depends(get_db)
):
    if q:
        return search_careers(db, q)

    return get_all_careers(db)


@router.get(
    "/{career_id}",
    response_model=CareerResponse
)
def get_career(
    career_id: int,
    db: Session = Depends(get_db)
):
    return get_career_by_id(career_id, db)