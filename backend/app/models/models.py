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
    Career_Industries,
    Careers,
    Skills, 
    Importance,
    Proficiency
)
# going to be making enums later on: 
# from sqlalchemy import Enum
# from app.utils.enums import (...)


class User(Base):
    __tablename__ = "users" 

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(String(30), nullable = False, unique = True) 

    email: Mapped[str] = mapped_column(String(40), nullable = False, unique = True) 

    role: Mapped[str] = mapped_column(Enum(UserRole), nullable = False, default = UserRole.USER)

    password_hash: Mapped[str] = mapped_column(String(255), nullable = False)

    is_active: Mapped[bool] = mapped_column(nullable = False, default = True)

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

    profile_visibility: Mapped[str] = mapped_column(Enum(ProfileVisibility), nullable = False, default = ProfileVisibility.PRIVATE)

    

class Student(Base): 
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), 
        nullable = False
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

    bio: Mapped[str] = mapped_column(String(1000))

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
        nullable = False
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

    bio: Mapped[str] = mapped_column(String(1000))

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




class Institution(Base):
    __tablename__ = "institutions"
    id: Mapped[int] = mapped_column(primary_key = True) 
    name: Mapped[str] = mapped_column(String(100), nullable = False)

    # rpi.edu
    domain: Mapped[str] = mapped_column(String(50), nullable = False)

    location: Mapped[str] = mapped_column(String(60), nullable = False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime( timezone = True ), 
        default = lambda: datetime.now(timezone.utc)
    )


class Degree(Base): 
    __tablename__ = "degrees"
    id: Mapped[int] = mapped_column(primary_key = True) 

    institution_id: Mapped[int] = mapped_column(ForeignKey("institutions.id"), nullable = False) 

    degree_type: Mapped[str] = mapped_column(Enum(DegreeType), nullable = False) 

    degree_name: Mapped[str] = mapped_column(String(200), nullable = False) 

    description: Mapped[str] = mapped_column(String(1000))

    total_credits: Mapped[int] = mapped_column(nullable = False) 

    created_at: Mapped[datetime] = mapped_column(
        DateTime( timezone = True ), 
        default = lambda: datetime.now(timezone.utc)
    )


class Course(Base): 
    __tablename__ = "courses"
    id: Mapped[int] = mapped_column(primary_key = True)

    institution_id: Mapped[int] = mapped_column(ForeignKey("institutions.id"), nullable = False) 

    code: Mapped[str] = mapped_column(String(20))

    name: Mapped[str] = mapped_column(String(100), nullable = False) 

    description: Mapped[str] = mapped_column(String(500))

    credits: Mapped[int] = mapped_column(nullable = False) 

    difficulty: Mapped[str] = mapped_column(Enum(CourseDifficulty), nullable = False) 

    created_at: Mapped[datetime] = mapped_column(
        DateTime( timezone = True ), 
        default = lambda: datetime.now(timezone.utc)
    )
    

class Student_Course(Base):
    __tablename__ = "student_courses"
    id: Mapped[int] = mapped_column(primary_key=True)

    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), nullable = False)

    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable = False)

    semester: Mapped[int] = mapped_column(Enum(StudentTerm), nullable = False)

    year: Mapped[int] = mapped_column(nullable = False) 

    grade: Mapped[str] = mapped_column(Enum(CourseGrade), nullable = False)

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

    semester: Mapped[int] = mapped_column(Enum(StudentTerm), nullable = False)

    year: Mapped[int] = mapped_column(nullable = False) 

    grade: Mapped[str] = mapped_column(Enum(CourseGrade), nullable = False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime( timezone = True ), 
        default = lambda: datetime.now(timezone.utc)
    )


class Career(Base): 
    __tablename__ = "careers" 
    id: Mapped[int] = mapped_column(primary_key = True) 

    title: Mapped[str] = mapped_column(Enum(Careers), nullable = False) 

    industry: Mapped[str] = mapped_column(Enum(Career_Industries), nullable = False) 

    description: Mapped[str] = mapped_column(String(1000), nullable = False) 

    salary_range: Mapped[str] = mapped_column(String(60))

    outlook: Mapped[str] = mapped_column(String(100))

    created_at: Mapped[datetime] = mapped_column(
        DateTime( timezone = True ), 
        default = lambda: datetime.now(timezone.utc)
    )
    

class Skill(Base): 
    __tablename__ = "skills"
    id: Mapped[int] = mapped_column(primary_key = True)

    name: Mapped[str] = mapped_column(Enum(Skills), nullable = False) 

    category: Mapped[str] = mapped_column(Enum(Career_Industries))

    description: Mapped[str] = mapped_column(String(1000), nullable = False) 


class Career_Skill(Base): 
    __tablename__ = "career_skills" 
    id: Mapped[int] = mapped_column(primary_key = True)

    career_id = Mapped[int] = mapped_column(ForeignKey("careers.id"), nullable = False) 

    skill_id = Mapped[int] = mapped_column(ForeignKey("skills.id"), nullable = False)

    importance = Mapped[int] = mapped_column(Enum(Importance), nullable = False) 

    description = Mapped[str] = mapped_column(String(1000))


class Student_Skill(Base): 
    __tablename__ = "student_skills" 
    id: Mapped[int] = mapped_column(primary_key = True) 

    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), nullable = False) 

    skill_id: Mapped[int] = mapped_column(ForeignKey("skills.id"), nullable = False) 

    proficiency: Mapped[str] = mapped_column(Enum(Proficiency), nullable = False) 

    learned_from: Mapped[str] = mapped_column(String(1000), nullable = False)



class Alumni_Skill(Base): 
    __tablename__ = "alumni_skills"
    id: Mapped[int] = mapped_column(primary_key = True)

    alumni_id: Mapped[int] = mapped_column(ForeignKey("alumni.id"), nullable = False)

    skill_id: Mapped[int] = mapped_column(ForeignKey("skills.id"), nullable = False)

    proficiency: Mapped[str] = mapped_column(Enum(Proficiency), nullable = False)

    learned_from: Mapped[str] = mapped_column(String(1000), nullable = False)


class Project(Base): 
    __tablename__ = "projects" 
    id: Mapped[int] = mapped_column(primary_key = True) 

    name: Mapped[str] = mapped_column(String(1000), nullable = False)

    description: Mapped[str] = mapped_column(String(2000), nullable = False)

    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), nullable = False) 

    visibility: Mapped[str] = mapped_column(Enum(ProfileVisibility), nullable = False)

    github_url: Mapped[str] = mapped_column(String(200))

    skill_id: Mapped[str] = mapped_column(ForeignKey("skills.id"), nullable = False) 

    created_at: Mapped[datetime] = mapped_column(
        DateTime( timezone = True ), 
        default = lambda: datetime.now(timezone.utc)
    )


"""
Dang I still need to add an alumni model I forgot


other possible models (look for relationships and back populate)




Need more parameters for user for sure

Users
Students
Alumni
Institutions
Courses
Careers
Skill
Degree
Pathways
Projects
Internships
Clubs
Audit

Need to have Identity, Gap Analysis, Targeting, Pathways

"""