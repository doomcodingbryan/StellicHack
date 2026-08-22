# matching_service.py 

from sqlalchemy.orm import Session

from app.models.models import (
    Student_Skill,
    Alumni_Career,
    Alumni_Skill
)


def match_alumni(
    student_id: int,
    career_id: int,
    db: Session,
    limit: int = 5
):

    student_skills = (
        db.query(Student_Skill)
        .filter(
            Student_Skill.student_id == student_id
        )
        .all()
    )

    student_skill_ids = {
        skill.skill_id
        for skill in student_skills
    }

    alumni_careers = (
        db.query(Alumni_Career)
        .filter(
            Alumni_Career.career_id == career_id
        )
        .all()
    )

    matches = []

    for alumni_career in alumni_careers:

        alumni_skills = (
            db.query(Alumni_Skill)
            .filter(
                Alumni_Skill.alumni_id ==
                alumni_career.alumni_id
            )
            .all()
        )

        alumni_skill_ids = {
            skill.skill_id
            for skill in alumni_skills
        }

        overlap = (
            student_skill_ids &
            alumni_skill_ids
        )

        score = len(overlap)

        matches.append({
            "alumni_id": alumni_career.alumni_id,
            "career_id": career_id,
            "matching_skills": len(overlap),
            "score": score
        })

    matches.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return matches[:limit]