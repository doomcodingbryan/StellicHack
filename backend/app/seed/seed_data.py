# seed_data.py

from sqlalchemy.orm import Session

from app.core.database import SessionLocal

from app.core.security import hash_password

from app.models.models import (
    User,
    Student,
    Alumni,
    Institution,
    Degree,
    Course,
    Career,
    Skill,
    Career_Skill,
    Student_Skill,
    Alumni_Skill,
    Alumni_Career
)

from app.utils.enums import (
    UserRole,
    ProfileVisibility,
    StudentTerm,
    StudentMajor,
    StudentYear,
    DegreeType,
    CourseDifficulty,
    Importance,
    Proficiency
)


def seed_database(db: Session):

    # =========================================================
    # INSTITUTION
    # =========================================================

    institution = (
        db.query(Institution)
        .filter(Institution.domain == "rpi.edu")
        .first()
    )

    if institution is None:

        institution = Institution(
            name="Rensselaer Polytechnic Institute",
            domain="rpi.edu",
            location="Troy, NY"
        )

        db.add(institution)
        db.flush()

    # =========================================================
    # DEGREE
    # =========================================================

    degree = (
        db.query(Degree)
        .filter(
            Degree.institution_id == institution.id,
            Degree.degree_name ==
            "Information Technology and Web Science"
        )
        .first()
    )

    if degree is None:

        degree = Degree(
            institution_id=institution.id,
            degree_type=DegreeType.BACHELOR,
            degree_name="Information Technology and Web Science",
            description=(
                "Bachelor's degree focused on information "
                "technology, web systems, and computing."
            ),
            total_credits=128
        )

        db.add(degree)
        db.flush()

    # =========================================================
    # CAREER
    # =========================================================

    career = (
        db.query(Career)
        .filter(
            Career.title == "Security Engineer"
        )
        .first()
    )

    if career is None:

        career = Career(
            title="Security Engineer",
            industry="Cybersecurity",
            description=(
                "Design, implement, and maintain secure "
                "systems, networks, infrastructure, and "
                "applications."
            ),
            salary_range="$80,000 - $150,000+",
            outlook="Strong"
        )

        db.add(career)
        db.flush()

    # =========================================================
    # SKILLS
    # =========================================================

    skill_data = [
        (
            "Linux",
            "Systems",
            "Linux administration, configuration, and security."
        ),
        (
            "Networking",
            "Networking",
            "TCP/IP, routing, switching, DNS, and network security."
        ),
        (
            "Python",
            "Programming",
            "Python programming and automation."
        ),
        (
            "C",
            "Programming",
            "C programming and low-level systems understanding."
        ),
        (
            "Cloud Security",
            "Cloud",
            "Security principles for cloud infrastructure."
        ),
        (
            "Network Security",
            "Security",
            "Firewalls, VPNs, segmentation, and secure networking."
        ),
        (
            "SQL",
            "Databases",
            "SQL database querying and data management."
        ),
        (
            "Git",
            "Development",
            "Version control using Git and GitHub."
        ),
    ]

    skills = {}

    for name, category, description in skill_data:

        skill = (
            db.query(Skill)
            .filter(Skill.name == name)
            .first()
        )

        if skill is None:

            skill = Skill(
                name=name,
                category=category,
                description=description
            )

            db.add(skill)
            db.flush()

        skills[name] = skill

    # =========================================================
    # CAREER SKILLS
    # =========================================================

    career_requirements = {
        "Linux": Importance.REQUIRED,
        "Networking": Importance.REQUIRED,
        "Python": Importance.FREQUENTLY_USED,
        "C": Importance.SOMEWHAT_IMPORTANT,
        "Cloud Security": Importance.REQUIRED,
        "Network Security": Importance.REQUIRED,
        "SQL": Importance.SOMEWHAT_IMPORTANT,
        "Git": Importance.FREQUENTLY_USED
    }

    for skill_name, importance in career_requirements.items():

        existing = (
            db.query(Career_Skill)
            .filter(
                Career_Skill.career_id == career.id,
                Career_Skill.skill_id ==
                skills[skill_name].id
            )
            .first()
        )

        if existing is None:

            db.add(
                Career_Skill(
                    career_id=career.id,
                    skill_id=skills[skill_name].id,
                    importance=importance,
                    description=(
                        f"{skill_name} is relevant to "
                        "the Security Engineer career."
                    )
                )
            )

    db.flush()

    # =========================================================
    # COURSES
    # =========================================================

    courses = [
        (
            "ITWS-2110",
            "Web Systems",
            "Web systems and application development.",
            4,
            CourseDifficulty.NEUTRAL
        ),
        (
            "CSCI-4210",
            "Operating Systems",
            "Operating systems, processes, threads, and systems programming.",
            4,
            CourseDifficulty.VERY_DIFFICULT
        ),
        (
            "CSCI-2500",
            "Computer Organization",
            "Computer architecture and low-level computing.",
            4,
            CourseDifficulty.VERY_DIFFICULT
        ),
        (
            "ITWS-4310",
            "Information Systems Security",
            "Information security concepts and practices.",
            3,
            CourseDifficulty.SOMEWHAT_DIFFICULT
        )
    ]

    for code, name, description, credits, difficulty in courses:

        existing = (
            db.query(Course)
            .filter(
                Course.institution_id == institution.id,
                Course.code == code
            )
            .first()
        )

        if existing is None:

            db.add(
                Course(
                    institution_id=institution.id,
                    code=code,
                    name=name,
                    description=description,
                    credits=credits,
                    difficulty=difficulty
                )
            )

    db.flush()

    # =========================================================
    # DEMO STUDENT USER
    # =========================================================

    student_user = (
        db.query(User)
        .filter(
            User.email == "student@example.com"
        )
        .first()
    )

    if student_user is None:

        student_user = User(
            username="demo_student",
            email="student@example.com",
            role=UserRole.STUDENT,
            password_hash=hash_password("password123"),
            profile_visibility=ProfileVisibility.PUBLIC
        )

        db.add(student_user)
        db.flush()

    # =========================================================
    # DEMO STUDENT PROFILE
    # =========================================================

    student = (
        db.query(Student)
        .filter(
            Student.user_id == student_user.id
        )
        .first()
    )

    if student is None:

        student = Student(
            user_id=student_user.id,
            institution_id=institution.id,
            degree_id=degree.id,
            grad_year=2027,
            grad_term=StudentTerm.SPRING,
            major=StudentMajor.INFORMATION_TECHNOLOGY,
            year=StudentYear.SENIOR,
            bio="Demo student for Pathfinder."
        )

        db.add(student)
        db.flush()

    # =========================================================
    # STUDENT SKILLS
    # =========================================================

    student_skill_data = {
        "Python": Proficiency.PROFICIENT,
        "Git": Proficiency.COMPETENT,
        "SQL": Proficiency.ADVANCED_BEGINNER
    }

    for skill_name, proficiency in student_skill_data.items():

        existing = (
            db.query(Student_Skill)
            .filter(
                Student_Skill.student_id == student.id,
                Student_Skill.skill_id ==
                skills[skill_name].id
            )
            .first()
        )

        if existing is None:

            db.add(
                Student_Skill(
                    student_id=student.id,
                    skill_id=skills[skill_name].id,
                    proficiency=proficiency
                )
            )

    # =========================================================
    # DEMO ALUMNI USER
    # =========================================================

    alumni_user = (
        db.query(User)
        .filter(
            User.email == "alumni@example.com"
        )
        .first()
    )

    if alumni_user is None:

        alumni_user = User(
            username="demo_alumni",
            email="alumni@example.com",
            role=UserRole.ALUMNI,
            password_hash=hash_password("password123"),
            profile_visibility=ProfileVisibility.PUBLIC
        )

        db.add(alumni_user)
        db.flush()

    # =========================================================
    # DEMO ALUMNI
    # =========================================================

    alumni = (
        db.query(Alumni)
        .filter(
            Alumni.user_id == alumni_user.id
        )
        .first()
    )

    if alumni is None:

        alumni = Alumni(
            user_id=alumni_user.id,
            institution_id=institution.id,
            degree_id=degree.id,
            grad_year=2024,
            grad_term=StudentTerm.SPRING,
            major=StudentMajor.INFORMATION_TECHNOLOGY,
            bio="Demo Pathfinder alumni.",
            current_company="Example Security",
            current_title="Security Engineer"
        )

        db.add(alumni)
        db.flush()

    # =========================================================
    # ALUMNI SKILLS
    # =========================================================

    alumni_skill_data = {
        "Linux": Proficiency.EXPERT,
        "Networking": Proficiency.EXPERT,
        "Python": Proficiency.PROFICIENT,
        "Cloud Security": Proficiency.PROFICIENT,
        "Network Security": Proficiency.EXPERT,
        "Git": Proficiency.PROFICIENT
    }

    for skill_name, proficiency in alumni_skill_data.items():

        existing = (
            db.query(Alumni_Skill)
            .filter(
                Alumni_Skill.alumni_id == alumni.id,
                Alumni_Skill.skill_id ==
                skills[skill_name].id
            )
            .first()
        )

        if existing is None:

            db.add(
                Alumni_Skill(
                    alumni_id=alumni.id,
                    skill_id=skills[skill_name].id,
                    proficiency=proficiency
                )
            )

    # =========================================================
    # ALUMNI CAREER
    # =========================================================

    existing_alumni_career = (
        db.query(Alumni_Career)
        .filter(
            Alumni_Career.alumni_id == alumni.id,
            Alumni_Career.career_id == career.id
        )
        .first()
    )

    if existing_alumni_career is None:

        db.add(
            Alumni_Career(
                alumni_id=alumni.id,
                career_id=career.id,
                company_name="Example Security",
                start_year=2024,
                is_current=True
            )
        )

    db.commit()

    print("Database seeded successfully.")


def main():

    db = SessionLocal()

    try:
        seed_database(db)
    finally:
        db.close()


if __name__ == "__main__":
    main()