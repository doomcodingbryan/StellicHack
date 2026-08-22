# pathway_service.py


from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.models import (
    Pathway,
    PathwayStep,
    Skill,
    Course
)
from app.services.gap_analysis_service import analyze_skill_gaps


def get_pathway_by_id(pathway_id: int, db: Session) -> Pathway:
    pathway = (
        db.query(Pathway)
        .filter(Pathway.id == pathway_id)
        .first()
    )

    if pathway is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pathway not found"
        )

    return pathway


def get_public_pathways_for_career(
    career_id: int,
    db: Session
) -> list[Pathway]:

    return (
        db.query(Pathway)
        .filter(
            Pathway.career_id == career_id,
            Pathway.is_public.is_(True)
        )
        .order_by(Pathway.id)
        .all()
    )


def add_pathway_step(
    pathway_id: int,
    data,
    db: Session
) -> PathwayStep:

    pathway = get_pathway_by_id(pathway_id, db)

    step = PathwayStep(
        pathway_id=pathway.id,
        step_number=data.step_number,
        title=data.title,
        description=data.description,
        step_type=data.step_type,
        course_id=data.course_id,
        project_id=data.project_id,
        internship_id=data.internship_id,
        resource_url=data.resource_url
    )

    db.add(step)
    db.commit()
    db.refresh(step)

    return step


def generate_pathway(
    student_id: int,
    career_id: int,
    db: Session
):
   

    gaps = analyze_skill_gaps(
        student_id,
        career_id,
        db
    )

    steps = []
    step_number = 1

    # skill gaps
    missing_skill_ids = [
        gap["skill_id"]
        for gap in gaps
        if gap["status"] == "missing"
    ]

    missing_skills = []

    if missing_skill_ids:
        missing_skills = (
            db.query(Skill)
            .filter(Skill.id.in_(missing_skill_ids))
            .order_by(Skill.name)
            .all()
        )

    for skill in missing_skills:

        steps.append({
            "step_number": step_number,
            "title": f"Develop {skill.name}",
            "description": (
                f"Build competency in {skill.name}, "
                "which is required for the selected career."
            ),
            "step_type": "Skill",
            "skill_id": skill.id,
            "course_id": None,
            "project_id": None,
            "internship_id": None,
            "resource_url": None
        })

        step_number += 1

    # recommended courses
    recommended_course_ids = set()

    for skill in missing_skills:

        courses = (
            db.query(Course)
            .filter(
                Course.name.ilike(f"%{skill.name}%")
            )
            .order_by(Course.code)
            .limit(2)
            .all()
        )

        for course in courses:

            if course.id in recommended_course_ids:
                continue

            recommended_course_ids.add(course.id)

            steps.append({
                "step_number": step_number,
                "title": f"Take {course.code}: {course.name}",
                "description": (
                    f"Recommended course for developing "
                    f"{skill.name}."
                ),
                "step_type": "Course",
                "skill_id": skill.id,
                "course_id": course.id,
                "project_id": None,
                "internship_id": None,
                "resource_url": None
            })

            step_number += 1

    # project
    if missing_skills:

        skill_names = ", ".join(
            skill.name for skill in missing_skills[:3]
        )

        steps.append({
            "step_number": step_number,
            "title": "Build a portfolio project",
            "description": (
                f"Build a project that demonstrates "
                f"{skill_names}. Add the project to your "
                "portfolio and GitHub."
            ),
            "step_type": "Project",
            "skill_id": None,
            "course_id": None,
            "project_id": None,
            "internship_id": None,
            "resource_url": None
        })

        step_number += 1

    # internship
    steps.append({
        "step_number": step_number,
        "title": "Gain professional experience",
        "description": (
            "Apply for internships or entry-level opportunities "
            "related to the selected career."
        ),
        "step_type": "Internship",
        "skill_id": None,
        "course_id": None,
        "project_id": None,
        "internship_id": None,
        "resource_url": None
    })

    step_number += 1


    # job 
    steps.append({
        "step_number": step_number,
        "title": "Apply for entry-level positions",
        "description": (
            "Use your completed coursework, projects, "
            "skills, and experience to apply for positions "
            "in this career."
        ),
        "step_type": "Job",
        "skill_id": None,
        "course_id": None,
        "project_id": None,
        "internship_id": None,
        "resource_url": None
    })

    return {
        "career_id": career_id,
        "student_id": student_id,
        "steps": steps
    }