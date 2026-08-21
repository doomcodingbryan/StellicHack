# careers.py

from fastapi import(
    APIRouter, 
    Depends, 
    HTTPException,
    status
)
from sqlalchemy.orm import Session
from app.core.database import SessionLocal 
from app.core.dependencies import(
    get_db, 
    get_current_user
)
from app.models.models import(
    User, 
    Careers
)
from app.schemas.schemas import(
    CareerCreate, 
    CareerResponse
)
from app.services.career_service import (
    get_career_by_id
)
from typing import Optional 
from fastapi import Query
from app.utils.enums import Careers, Career_Industries 

router = APIRouter(
    prefix = "/careers", 
    tags = ["Careers"]
)


# @router.post(
#     "", 
#     response_model = CareerResponse, 
#     status_code = status.HTTP_201_CREATED
# )
# # creating a career, needed? Better than an enum since there are so many? 
# def create_career(
#     career: CareerCreate, 
#     db: Session = Depends(get_db), 
#     current_user: User = Depends(get_current_user)
# ): 