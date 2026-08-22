# institutions.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.models.models import Institution
from app.schemas.schemas import InstitutionResponse


router = APIRouter(
    prefix="/institutions",
    tags=["Institutions"]
)


@router.get(
    "",
    response_model=list[InstitutionResponse]
)
def get_institutions(
    db: Session = Depends(get_db)
):
    return (
        db.query(Institution)
        .order_by(Institution.name)
        .all()
    )


@router.get(
    "/{institution_id}",
    response_model=InstitutionResponse
)
def get_institution(
    institution_id: int,
    db: Session = Depends(get_db)
):

    institution = (
        db.query(Institution)
        .filter(Institution.id == institution_id)
        .first()
    )

    if institution is None:
        from fastapi import HTTPException, status

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Institution not found"
        )

    return institution