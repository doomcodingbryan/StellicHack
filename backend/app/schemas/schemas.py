# schemas.py
# blueprints for endpoints


from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime
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



class UserCreate(BaseModel):
    username: str
    email: EmailStr
    role: UserRole
    password: str
    profile_visibility: ProfileVisibility

class UserResponse(BaseModel): 

    model_config = ConfigDict(from_attributes = True)

    id: int
    username: str
    email: EmailStr
    role: UserRole 
    profile_visibility: ProfileVisibility

class Token(BaseModel): 
    access_token: str
    token_type: str

# how to make the student schema? Because once the user selects their
# role from creation, it should either: Ask them to fill out the other 
# fields needed for that role, or have them go through regularly as a normal user (not student or alumn)
class StudentCreate(BaseModel): 
    institution_id: int
    degree_id: int
    grad_year: int
    grad_term: StudentTerm
    major: StudentMajor 
    year: StudentYear
    bio: str | None = None

class StudentResponse(BaseModel): 
    model_config = ConfigDict(from_attributes = True) 

    id: int
    user_id: int 
    institution_id: int 
    degree_id: int
    grad_year: int 
    grad_term: StudentTerm
    major: StudentMajor
    year: StudentYear
    bio: str | None



class InstitutionCreate(BaseModel): 
    name: str
    domain: str
    location: str

class InstitutionResponse(BaseModel): 
    model_config = ConfigDict(from_attributes = True)

    id: int
    name: str
    domain: str
    location: str



class DegreeCreate(BaseModel): 
    # also something like institution id like the line below is a foreign key, is that
    # defined properly below? Is it done a different way? Do we have to do it at all? 
    # also I feel like a foreign key like this would have to be inputted by the user 
    # but if they're logged in and the student account already has an instituion id they are 
    # connected to then.... how would I properly implement this foreign key? Just not put it at all it seems
    institution_id: int
    degree_type: DegreeType
    degree_name: str
    description: str
    total_credits: int

class DegreeResponse(BaseModel): 
    model_config = ConfigDict(from_attributes = True)

    id: int
    institution_id: int
    degree_type: DegreeType
    degree_name: str
    description: str
    total_credits: int



class CourseCreate(BaseModel): 
    institution_id: int
    code: str
    name: str 
    description: str
    credits: int 
    difficulty: CourseDifficulty

class CourseResponse(BaseModel): 
    model_config = ConfigDict(from_attributes=True)

    id: int
    institution_id: int
    code: str
    name: str
    description: str 
    credits: int
    difficulty: CourseDifficulty



class CareerCreate(BaseModel): 
    title: str
    industry: str
    description: str
    salary_range: str | None = None
    outlook: str | None = None

class CareerResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    industry: str
    description: str
    salary_range: str | None
    outlook: str | None



class SkillCreate(BaseModel):
    name: str
    category: str
    description: str | None = None

class SkillResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    category: str
    description: str | None



class ProjectCreate(BaseModel):
    name: str
    description: str
    visibility: ProfileVisibility
    github_url: str | None = None

class ProjectResponse(BaseModel): 
    model_config = ConfigDict(from_attributes = True) 

    id: int
    name: str
    description: str
    visibility: ProfileVisibility
    github_url: str | None


class StudentCourseCreate(BaseModel): 
    course_id: int
    semester: StudentTerm
    year: int
    grade: CourseGrade | None = None
    status: CourseStatus

class StudentCourseResponse(BaseModel): 
    model_config = ConfigDict(from_attributes=True)

    id: int
    course_id: int 
    semester: StudentTerm 
    year: int
    grade: CourseGrade | None
    status: CourseStatus


class StudentSkillCreate(BaseModel): 
    skill_id: int
    proficiency: Proficiency

class StudentSkillResponse(BaseModel): 
    model_config = ConfigDict(from_attributes=True)

    skill_id: int
    proficiency: Proficiency


class AlumniSkillCreate(BaseModel): 
    skill_id: int
    proficiency: Proficiency

class AlumniSkillResponse(BaseModel): 
    model_config = ConfigDict(from_attributes=True)

    skill_id: int
    proficiency: Proficiency


class PathwayStepCreate(BaseModel):
    step_number: int
    title: str
    description: str 
    step_type: StepType
    course_id: int | None = None
    project_id: int | None = None
    internship_id: int | None = None
    resource_url: str | None = None

class PathwayStepResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    step_number: int
    title: str
    description: str
    step_type: StepType
    course_id: int | None
    project_id: int | None
    internship_id: int | None
    resource_url: str | None


class PathwayCreate(BaseModel):
    career_id: int
    title: str
    description: str | None = None
    is_public: bool = True

class PathwayResponse(BaseModel): 
    model_config = ConfigDict(from_attributes = True) 

    id: int
    career_id: int
    title: str
    description: str | None
    is_public: bool

"""

Other than the questions above, how do I go about making the schemas 
for the student_course, career_skill, student_skill (and alumni) classes in models? 
Do I need to make them? 

"""