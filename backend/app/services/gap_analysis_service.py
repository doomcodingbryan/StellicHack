# gap_analysis_service.py 

from sqlalchemy.orm import Session

from app.models.models import (
    Career_Skill,
    Student_Skill
)

from app.utils.enums import (
    Importance,
    Proficiency
)


def analyze_skill_gaps(
    student_id: int,
    career_id: int,
    db: Session
):

    required = (
        db.query(Career_Skill)
        .filter(Career_Skill.career_id == career_id)
        .all()
    )

    student_skills = (
        db.query(Student_Skill)
        .filter(Student_Skill.student_id == student_id)
        .all()
    )

    student_skill_map = {
        item.skill_id: item.proficiency
        for item in student_skills
    }

    gaps = []

    for requirement in required:

        student_proficiency = student_skill_map.get(
            requirement.skill_id
        )

        if student_proficiency is None:

            gaps.append({
                "skill_id": requirement.skill_id,
                "status": "missing",
                "importance": requirement.importance.value,
                "current_proficiency": None
            })

        else:

            gaps.append({
                "skill_id": requirement.skill_id,
                "status": "has_skill",
                "importance": requirement.importance.value,
                "current_proficiency": student_proficiency.value
            })

    return gaps


def calculate_career_match_score(
    student_id: int,
    career_id: int,
    db: Session
):

    required = (
        db.query(Career_Skill)
        .filter(Career_Skill.career_id == career_id)
        .all()
    )

    student_skills = (
        db.query(Student_Skill)
        .filter(Student_Skill.student_id == student_id)
        .all()
    )

    student_skill_map = {
        item.skill_id: item.proficiency
        for item in student_skills
    }

    if not required:
        return 0

    importance_weights = {
        Importance.NOT_IMPORTANT: 1,
        Importance.SOMEWHAT_IMPORTANT: 2,
        Importance.FREQUENTLY_USED: 3,
        Importance.REQUIRED: 4
    }

    proficiency_scores = {
        Proficiency.LEARNING: 1,
        Proficiency.NOVICE: 2,
        Proficiency.ADVANCED_BEGINNER: 3,
        Proficiency.COMPETENT: 4,
        Proficiency.PROFICIENT: 5,
        Proficiency.EXPERT: 6
    }

    score = 0
    total = 0

    for requirement in required:

        weight = importance_weights.get(
            requirement.importance,
            1
        )

        total += 6 * weight

        proficiency = student_skill_map.get(
            requirement.skill_id
        )

        if proficiency is not None:

            level = proficiency_scores.get(
                proficiency,
                0
            )

            score += level * weight

    if total == 0:
        return 0

    return round(
        (score / total) * 100
    )