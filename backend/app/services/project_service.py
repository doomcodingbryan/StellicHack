# project_service.py 

from fastapi import HTTPException, status
from sqlalchemy.orm import Session 
from app.models.models import Project

def create_student_project(student_id: int, data, db: Session)->Project: 
    project = Project(
        student_id = student_id, 
        name = data.name, 
        description = data.description, 
        visibility = data.visibility, 
        github_url = data.github_url
    )

    db.add(project)
    db.commit()
    db.refresh(project) 

    return project

def get_student_projects(student_id: int, db: Session) -> list[Project]: 
    return(db.query(Project).filter(Project.student_id == student_id).order_by(Project.created_at.desc()).all())

def get_project_by_id(project_id: int, db: Session)->Project: 
    project = (db.query(Project).filter(Project.id == project_id).first())

    if project is None: 
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = "Project not found" 
        )

    return project
