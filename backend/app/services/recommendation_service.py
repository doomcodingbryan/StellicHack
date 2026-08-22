from sqlalchemy.orm import Session

from app.models.models import Skill, Course
from app.services.gap_analysis_service import analyze_skill_gaps


def recommended_courses(
    student_id: int,
    career_id: int,
    db: Session
):
    gaps = analyze_skill_gaps(
        student_id,
        career_id,
        db
    )

    missing_skill_ids = [
        gap["skill_id"]
        for gap in gaps
        if gap["status"] == "missing"
    ]

    if not missing_skill_ids:
        return []

    skills = (
        db.query(Skill)
        .filter(Skill.id.in_(missing_skill_ids))
        .order_by(Skill.name)
        .all()
    )

    recommendations = []
    added_course_ids = set()

    for skill in skills:

        courses = (
            db.query(Course)
            .filter(
                Course.name.ilike(f"%{skill.name}%")
            )
            .order_by(Course.code)
            .limit(3)
            .all()
        )

        for course in courses:

            if course.id in added_course_ids:
                continue

            added_course_ids.add(course.id)

            recommendations.append(course)

    return recommendations