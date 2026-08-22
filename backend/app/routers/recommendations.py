from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.models import User

from app.core.dependencies import (
    get_db,
    get_current_user
)

from app.services.student_service import (
    get_student_for_user
)

from app.services.gap_analysis_service import (
    analyze_skill_gaps,
    calculate_career_match_score
)

from app.services.matching_service import (
    match_alumni
)

from app.services.pathway_service import (
    generate_pathway
)

from app.services.recommendation_service import (
    recommended_courses
)


router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


@router.get("/careers/{career_id}/gaps")
def career_gaps(
    career_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    student = get_student_for_user(
        current_user.id,
        db
    )

    gaps = analyze_skill_gaps(
        student.id,
        career_id,
        db
    )

    score = calculate_career_match_score(
        student.id,
        career_id,
        db
    )

    return {
        "career_id": career_id,
        "match_score": score,
        "gaps": gaps
    }


@router.get("/careers/{career_id}/alumni")
def career_alumni_matches(
    career_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    student = get_student_for_user(
        current_user.id,
        db
    )

    return match_alumni(
        student.id,
        career_id,
        db
    )


@router.get("/careers/{career_id}/courses")
def career_course_recommendations(
    career_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    student = get_student_for_user(
        current_user.id,
        db
    )

    return recommended_courses(
        student.id,
        career_id,
        db
    )


@router.get("/careers/{career_id}/pathway")
def career_pathway(
    career_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    student = get_student_for_user(
        current_user.id,
        db
    )

    return generate_pathway(
        student.id,
        career_id,
        db
    )