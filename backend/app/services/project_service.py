# project_service.py

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.models import Project

def get_project_by_id( project_id: int, db: Session) -> Project: 
    project = (db.query(Project).filter(Project.id == project_id).first())
    if project is None: 
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Asset not found" 
        )
    return project