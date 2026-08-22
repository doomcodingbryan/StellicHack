# pathways.py 

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.schemas import (
    PathwayCreate,
    PathwayResponse,
    PathwayStepCreate,
    PathwayStepResponse
)

from app.services.pathway_service import (
    get_pathway_by_id,
    get_public_pathways_for_career,
    add_pathway_step
)

from app.models.models import Pathway


router = APIRouter(
    prefix="/pathways",
    tags=["Pathways"]
)


@router.get(
    "/careers/{career_id}",
    response_model=list[PathwayResponse]
)
def get_career_pathways(
    career_id: int,
    db: Session = Depends(get_db)
):

    return get_public_pathways_for_career(
        career_id,
        db
    )


@router.get(
    "/{pathway_id}",
    response_model=PathwayResponse
)
def get_pathway(
    pathway_id: int,
    db: Session = Depends(get_db)
):

    return get_pathway_by_id(
        pathway_id,
        db
    )


@router.post(
    "",
    response_model=PathwayResponse,
    status_code=status.HTTP_201_CREATED
)
def create_pathway(
    data: PathwayCreate,
    db: Session = Depends(get_db)
):

    pathway = Pathway(
        career_id=data.career_id,
        title=data.title,
        description=data.description,
        is_public=data.is_public
    )

    db.add(pathway)
    db.commit()
    db.refresh(pathway)

    return pathway


@router.post(
    "/{pathway_id}/steps",
    response_model=PathwayStepResponse,
    status_code=status.HTTP_201_CREATED
)
def create_pathway_step(
    pathway_id: int,
    data: PathwayStepCreate,
    db: Session = Depends(get_db)
):

    return add_pathway_step(
        pathway_id,
        data,
        db
    )