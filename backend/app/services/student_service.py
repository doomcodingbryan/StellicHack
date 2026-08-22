# student_service.py 

from fastapi import HTTPException, status
from sqlalchemy.orm import Session 
from app.models.models import Student, Student_Course, Project, Student_Skill


# use student = get_student_for_user(current_user.id, db)
def get_student_for_user(user_id: int, db: Session) -> Student: 
    student = (db.query(Student).filter(Student.user_id==user_id).first())

    if student is None: 
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = "Student profile not found" 
        )

    return student


def get_student_courses(student_id: int, db: Session): 
    return(db.query(Student_Course).filter(Student_Course.student_id == student_id).all())


def get_student_skills(student_id: int, db: Session): 
    return (db.query(Student_Skill).filter(Student_Skill.student_id == student_id).all())


def get_student_projects(student_id: int, db:Session): 
    return(db.query(Project).filter(Project.student_id == student_id).all())


def create_student_profile (
    user_id: int, 
    data, 
    db:Session
): 
    existing = (db.query(Student).filter(Student.user_id == user_id).first())

    if existing: 
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, 
            detail = "Student profile already exists"
        )

    student = Student (
        user_id = user_id, 
        institution_id = data.institution_id, 
        degree_id = data.degree_id, 
        grad_year = data.grad_year, 
        grad_term = data.grad_term, 
        major = data.major,
        year = data.year, 
        bio = data.bio
    )

    db.add(student) 
    db.commit()
    db.refresh(student)

    return student