# skills.py 

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.models.models import Skill
from app.schemas.schemas import SkillResponse

router = APIRouter(
    prefix="/skills",
    tags=["Skills"]
)


@router.get(
    "",
    response_model=list[SkillResponse]
)
def get_skills(
    db: Session = Depends(get_db)
):
    return (
        db.query(Skill)
        .order_by(Skill.name)
        .all()
    )