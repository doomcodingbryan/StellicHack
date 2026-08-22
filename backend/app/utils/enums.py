# enums.py

from enum import Enum

class UserRole (str, Enum):
    STUDENT = "Student"
    ALUMNI = "Alumni"
    USER = "User"
    ADMIN = "Admin"

class ProfileVisibility(str, Enum): 
    PUBLIC = "Public"
    PRIVATE = "Private"





class StudentTerm(str, Enum): 
    FALL = "Fall"
    SPRING = "Spring" 
    SUMMER = "Summer"

class StudentMajor(str, Enum): 
    BIOLOGY  = "Biology"
    COMPUTER_SCIENCE = "Computer Science"
    BIOMEDICAL_ENGINEERING = "Biomedical Engineering"
    BUSINESS = "Business"
    INFORMATION_TECHNOLOGY = "Information Technology"
    MECHANICAL_ENGINEERING = "Mechanical Engineering"
    ELECTRICAL_ENGINEERING = "Electrical Engineering"
    CIVIL_ENGINEERING = "Civil Engineering" 
    COMPUTER_ENGINEERING = "Computer Engineering"
    CHEMICAL_ENGINEERING = "Chemical Engineering" 
    AEROSPACE_ENGINEERING = "Aerospace Engineering"
    INDUSTRIAL_ENGINEERING = "Industrial Engineering"
    SYSTEMS_ENGINEERING = "Systems Engineering" 
    ENVIRONMENTAL_ENGINEERING = "Environmental Engineering" 
    SPORTS_MANAGEMENT = "Sports Management"
    PHARMACY = "Pharmacy" 
    PHYSICAL_THERAPY = "Physical Therapy"
    OCCUPATIONAL_THERAPY = "Occupational Therapy" 
    KINESIOLOGY = "Kinesiology"
    PSYCHOLOGY = "Psychology" 
    HISTORY = "History" 
    ECONOMICS = "Economics" 
    PHILOSOPHY = "Philosophy"
    EDUCATION = "Education" 
    MATHEMATICS = "Mathematics"

class StudentYear(str, Enum): 
    FRESHMAN = "Freshman"
    SOPHOMORE = "Sophomore"
    JUNIOR = "Junior" 
    SENIOR = "Senior"

class DegreeType(str, Enum): 
    ASSOCIATE = "Associate"
    BACHELOR = "Bachelor"
    MASTER = "Master" 
    DOCTORATE = "Doctorate" 
    PROFESSIONAL = "Professional" 


class CourseDifficulty(str, Enum): 
    EASY = "Easy"
    SOMEWHAT_EASY = "Somewhat Easy"
    NEUTRAL = "Neutral"
    SOMEWHAT_DIFFICULT = "Somewhat Difficult"
    VERY_DIFFICULT = "Very Difficult"
    DO_NOT_TAKE = "Do Not Take"


class CourseGrade(str, Enum): 
    A_PLUS = "A+"
    A = "A"
    A_MINUS = "A-"
    B_PLUS = "B+"
    B = "B"
    B_MINUS = "B-"
    C_PLUS = "C+"
    C = "C"
    C_MINUS = "C-"
    D_PLUS = "D+"
    D = "D"
    D_MINUS = "D-"
    F = "F"


class CourseStatus(str, Enum): 
    NOT_STARTED = "Not Started" 
    IN_PROGRESS = "In Progress" 
    COMPLETED = "Completed"
    DROPPED = "Dropped"



class Importance(str, Enum): 
    NOT_IMPORTANT = "Not Important" 
    SOMEWHAT_IMPORTANT = "Somewhat Important" 
    REQUIRED = "Required" 
    FREQUENTLY_USED = "Frequently Used"


class Proficiency(str, Enum): 
    LEARNING = "Learning" 
    NOVICE = "Novice" 
    ADVANCED_BEGINNER = "Advanced Beginner" 
    COMPETENT = "Competent" 
    PROFICIENT = "Proficient" 
    EXPERT = "Expert" 
    

class StepType(str, Enum): 
    COURSE = "Course"
    PROJECT = "Project"
    INTERNSHIP = "Internship"
    CLUB = "Club" 
    CERTIFICATION = "Certification"
    SKILL = "Skill"
    JOB = "Job"
    OTHER = "Other"
