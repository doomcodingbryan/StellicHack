# models.py 
# create the db tables and what they look like
# use sqlalchemy for convenience

from sqlalchemy import String, Integer, ForeignKey, DateTime
from datetime import datetime, timezone
#import Base created from database.py 
from app.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum
from app.utils.enums import(
    UserRole,
    ProfileVisibility, 
    StudentTerm, 
    StudentMajor,
    StudentYear, 
    DegreeType,
    CourseDifficulty, 
    CourseGrade, 
    CourseStatus,
    StepType, 
    Importance,
    Proficiency
)
# going to be making enums later on: 
# from sqlalchemy import Enum
# from app.utils.enums import (...)

# final user model
class User(Base):
    __tablename__ = "users" 

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(String(30), nullable = False, unique = True) 

    email: Mapped[str] = mapped_column(String(255), nullable = False, unique = True) 

    role: Mapped[str] = mapped_column(Enum(UserRole), nullable = False, default = UserRole.USER)

    password_hash: Mapped[str] = mapped_column(String(255), nullable = False)

    is_active: Mapped[bool] = mapped_column(nullable = False, default = True)

    profile_visibility: Mapped[str] = mapped_column(Enum(ProfileVisibility), nullable = False, default = ProfileVisibility.PRIVATE)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone = True), 

        default = lambda: datetime.now(timezone.utc)
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime ( timezone = True ), 
        default = lambda: datetime.now(timezone.utc), 
        onupdate = lambda: datetime.now(timezone.utc)
    )


    

class Student(Base): 
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), 
        nullable = False, 
        unique = True
    )

    institution_id: Mapped[int] = mapped_column(
        ForeignKey("institutions.id"), 
        nullable = False
    )

    degree_id: Mapped[int] = mapped_column(
        ForeignKey("degrees.id"), 
        nullable = False
    )

    grad_year: Mapped[int] = mapped_column(
        nullable = False
    )

    grad_term: Mapped[str] = mapped_column(Enum(StudentTerm), nullable = False) 

    major: Mapped[str] = mapped_column(
        Enum(StudentMajor),
        nullable = False
    )

    year: Mapped[str] = mapped_column(
        Enum(StudentYear),
        nullable = False
    )

    bio: Mapped[str | None] = mapped_column(String(1000))

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone = True), 

        # may need to fix this line
        default = lambda: datetime.now(timezone.utc)
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime ( timezone = True ), 
        default = lambda: datetime.now(timezone.utc), 
        onupdate = lambda: datetime.now(timezone.utc)
    )



class Alumni(Base): 
    __tablename__ = "alumni"
    id: Mapped[int] = mapped_column(primary_key = True) 

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), 
        nullable = False, 
        unique = True
    )

    institution_id: Mapped[int] = mapped_column(
        ForeignKey("institutions.id"), 
        nullable = False
    )

    degree_id: Mapped[int] = mapped_column(
        ForeignKey("degrees.id"), 
        nullable = False
    )

    grad_year: Mapped[int] = mapped_column(
        nullable = False
    )

    grad_term: Mapped[str] = mapped_column(Enum(StudentTerm), nullable = False) 

    major: Mapped[str] = mapped_column(
        Enum(StudentMajor),
        nullable = False
    )

    bio: Mapped[str | None] = mapped_column(String(1000))

    current_company: Mapped[str | None] = mapped_column(String(200))

    current_title: Mapped[str | None] = mapped_column(String(200))

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone = True), 

        # may need to fix this line
        default = lambda: datetime.now(timezone.utc)
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime ( timezone = True ), 
        default = lambda: datetime.now(timezone.utc), 
        onupdate = lambda: datetime.now(timezone.utc)
    )



# only get function needed for students and alumns
class Institution(Base):
    __tablename__ = "institutions"
    id: Mapped[int] = mapped_column(primary_key = True) 
    name: Mapped[str] = mapped_column(String(100), nullable = False, unique = True)

    # rpi.edu
    domain: Mapped[str] = mapped_column(String(50), nullable = False)

    location: Mapped[str] = mapped_column(String(60), nullable = False)


# must recheck the foreign key logic, will it be auto filled out
# properly this way ? 
class Degree(Base): 
    __tablename__ = "degrees"
    id: Mapped[int] = mapped_column(primary_key = True) 

    institution_id: Mapped[int] = mapped_column(ForeignKey("institutions.id"), nullable = False) 

    degree_type: Mapped[str] = mapped_column(Enum(DegreeType), nullable = False) 

    degree_name: Mapped[str] = mapped_column(String(200), nullable = False) 

    description: Mapped[str | None] = mapped_column(String(1000))

    total_credits: Mapped[int] = mapped_column(nullable = False) 

    created_at: Mapped[datetime] = mapped_column(
        DateTime( timezone = True ), 
        default = lambda: datetime.now(timezone.utc)
    )


class Course(Base): 
    __tablename__ = "courses"
    id: Mapped[int] = mapped_column(primary_key = True)

    institution_id: Mapped[int] = mapped_column(ForeignKey("institutions.id"), nullable = False) 

    code: Mapped[str | None] = mapped_column(String(20))

    name: Mapped[str] = mapped_column(String(100), nullable = False) 

    description: Mapped[str | None] = mapped_column(String(500))

    credits: Mapped[int] = mapped_column(nullable = False) 

    difficulty: Mapped[str] = mapped_column(Enum(CourseDifficulty), nullable = False) 

    created_at: Mapped[datetime] = mapped_column(
        DateTime( timezone = True ), 
        default = lambda: datetime.now(timezone.utc)
    )
    

# need a junction table, backdate? Fine how it is? 
# array for the students that take a specific course, etc. 
class Student_Course(Base):
    __tablename__ = "student_courses"
    id: Mapped[int] = mapped_column(primary_key=True)

    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), nullable = False)

    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable = False)

    semester: Mapped[str] = mapped_column(Enum(StudentTerm), nullable = False)

    year: Mapped[int] = mapped_column(nullable = False) 

    grade: Mapped[str] = mapped_column(Enum(CourseGrade), nullable = True)

    status: Mapped[str] = mapped_column(Enum(CourseStatus), nullable = False) 

    created_at: Mapped[datetime] = mapped_column(
        DateTime( timezone = True ), 
        default = lambda: datetime.now(timezone.utc)
    )



class Alumni_Course(Base):
    __tablename__ = "alumni_courses"
    id: Mapped[int] = mapped_column(primary_key=True)

    alumni_id: Mapped[int] = mapped_column(ForeignKey("alumni.id"), nullable = False)

    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable = False)

    semester: Mapped[str] = mapped_column(Enum(StudentTerm), nullable = False)

    year: Mapped[int] = mapped_column(nullable = False) 

    grade: Mapped[str] = mapped_column(Enum(CourseGrade), nullable = False)

    status: Mapped[str] = mapped_column(Enum(CourseStatus), nullable = False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime( timezone = True ), 
        default = lambda: datetime.now(timezone.utc)
    )


# too restrictive right now
class Career(Base): 
    __tablename__ = "careers" 
    id: Mapped[int] = mapped_column(primary_key = True) 

    title: Mapped[str] = mapped_column(String(150), nullable = False, unique = True) 

    industry: Mapped[str] = mapped_column(String(200), nullable = False) 

    description: Mapped[str] = mapped_column(String(1000), nullable = False) 

    salary_range: Mapped[str | None] = mapped_column(String(60))

    outlook: Mapped[str | None] = mapped_column(String(100))

    created_at: Mapped[datetime] = mapped_column(
        DateTime( timezone = True ), 
        default = lambda: datetime.now(timezone.utc)
    )
    

class Skill(Base): 
    __tablename__ = "skills"
    id: Mapped[int] = mapped_column(primary_key = True)

    name: Mapped[str] = mapped_column(String(150), nullable = False, unique = True) 

    category: Mapped[str] = mapped_column(String(100), nullable = False)

    description: Mapped[str] = mapped_column(String(1000), nullable = False) 

    created_at: Mapped[datetime] = mapped_column(
        DateTime( timezone = True ), 
        default = lambda: datetime.now(timezone.utc)
    )


class Career_Skill(Base):
    __tablename__ = "career_skills"

    id: Mapped[int] = mapped_column(primary_key=True)

    career_id: Mapped[int] = mapped_column(
        ForeignKey("careers.id"),
        nullable=False
    )

    skill_id: Mapped[int] = mapped_column(
        ForeignKey("skills.id"),
        nullable=False
    )

    importance: Mapped[Importance] = mapped_column(
        Enum(Importance),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        String(1000)
    )

class Student_Skill(Base): 
    __tablename__ = "student_skills" 
    id: Mapped[int] = mapped_column(primary_key = True) 

    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), nullable = False) 

    skill_id: Mapped[int] = mapped_column(ForeignKey("skills.id"), nullable = False) 

    proficiency: Mapped[str] = mapped_column(Enum(Proficiency), nullable = False) 

    created_at: Mapped[datetime] = mapped_column(
        DateTime( timezone = True ), 
        default = lambda: datetime.now(timezone.utc)
    )


class Alumni_Skill(Base): 
    __tablename__ = "alumni_skills"
    id: Mapped[int] = mapped_column(primary_key = True)

    alumni_id: Mapped[int] = mapped_column(ForeignKey("alumni.id"), nullable = False)

    skill_id: Mapped[int] = mapped_column(ForeignKey("skills.id"), nullable = False)

    proficiency: Mapped[str] = mapped_column(Enum(Proficiency), nullable = False)


class Alumni_Career(Base): 
    __tablename__ = "alumni_careers"
    id: Mapped[int] = mapped_column(primary_key = True) 

    alumni_id: Mapped[int] = mapped_column(
        ForeignKey("alumni.id"),
        nullable=False
    )

    career_id: Mapped[int] = mapped_column( ForeignKey("careers.id"), nullable = False) 

    company_name: Mapped[str | None] = mapped_column(String(150))

    start_year: Mapped[int | None] = mapped_column()

    end_year: Mapped[int | None] = mapped_column()

    is_current: Mapped[bool] = mapped_column(nullable = False, default = True) 


class Project(Base): 
    __tablename__ = "projects" 
    id: Mapped[int] = mapped_column(primary_key = True) 

    student_id: Mapped[int | None] = mapped_column(ForeignKey("students.id"), nullable = True)

    alumni_id: Mapped[int | None] = mapped_column(ForeignKey("alumni.id"), nullable = True) 

    name: Mapped[str] = mapped_column(String(300), nullable = False)

    description: Mapped[str] = mapped_column(String(2000), nullable = False)

    visibility: Mapped[str] = mapped_column(Enum(ProfileVisibility), nullable = False, default = ProfileVisibility.PRIVATE)

    github_url: Mapped[str | None] = mapped_column(String(500))

    created_at: Mapped[datetime] = mapped_column(
        DateTime( timezone = True ), 
        default = lambda: datetime.now(timezone.utc)
    )


class Internship(Base): 
    __tablename__ = "internships" 
    id: Mapped[int] = mapped_column(primary_key = True) 

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable = False)

    company_name: Mapped[str] = mapped_column(String(150), nullable = False)

    title: Mapped[str] = mapped_column(String(150), nullable = False) 

    description: Mapped[str | None] = mapped_column(String(1000))

    start_date: Mapped[datetime | None] = mapped_column(DateTime(timezone = True))

    end_date: Mapped[datetime | None] = mapped_column(DateTime(timezone = True))

    created_at: Mapped[datetime] = mapped_column(
        DateTime( timezone = True ), 
        default = lambda: datetime.now(timezone.utc)
    )


class Pathway(Base): 
    __tablename__ = "pathways" 

    id: Mapped[int] = mapped_column(primary_key = True) 

    alumni_id: Mapped[int] = mapped_column(ForeignKey("alumni.id"), nullable = True)

    career_id: Mapped[int] = mapped_column(ForeignKey("careers.id"), nullable = False)

    title: Mapped[str] = mapped_column(String(200), nullable = False) 

    description: Mapped[str | None] = mapped_column(String(1500), nullable = True)

    is_public: Mapped[bool] = mapped_column(nullable = False, default = True) 

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default = lambda: datetime.now(timezone.utc))


class PathwayStep(Base): 
    __tablename__ = "pathway_steps"

    id: Mapped[int] = mapped_column(primary_key = True)

    pathway_id: Mapped[int] = mapped_column(ForeignKey("pathways.id"), nullable = False)

    step_number: Mapped[int] = mapped_column(nullable = False) 

    title: Mapped[str] = mapped_column(String(200), nullable=False) 

    description: Mapped[str] = mapped_column(String(1000), nullable = False) 

    step_type: Mapped[str] = mapped_column(Enum(StepType), nullable = False) 

    course_id: Mapped[int | None] = mapped_column(ForeignKey("courses.id"), nullable = True) 

    project_id: Mapped[int | None] = mapped_column(ForeignKey("projects.id"), nullable = True) 

    internship_id: Mapped[int | None] = mapped_column(ForeignKey("internships.id"), nullable = True) 

    resource_url: Mapped[str | None] = mapped_column(String(500), nullable = True)
