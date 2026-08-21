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
    Career_Industries,
    Careers,
    Skills, 
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
    title: Careers
    industy: Career_Industries
    description: str
    # forgot about optional information, how do I write it for that on the schemas? Will it allow them to not put anything since it is nullable
    # even though I put it here on the schema? 
    salary_range: str
    outlook: str

class CareerResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: Careers
    industry: Career_Industries
    description: str



class SkillCreate(BaseModel):
    name: Skills
    category: Career_Industries
    description: str

class SkillResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: Skills
    category: Career_Industries
    description: str



class ProjectCreate(BaseModel):
    name: str
    description: str
    visibility: ProfileVisibility
    github_url: str 

class ProjectResponse(BaseModel): 
    name: str
    description: str
    visibilty: ProfileVisibility
    github_url: str


"""
Other than the questions above, how do I go about making the schemas 
for the student_course, career_skill, student_skill (and alumni) classes in models? 
Do I need to make them? 

"""