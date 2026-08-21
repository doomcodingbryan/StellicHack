# enums.py

from enum import Enum

class UserRole (str, Enum):
    STUDENT = "Student"
    ALUMNI = "Alumni"
    USER = "User"

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



class Career_Industries(str, Enum): 
    TECHNOLOGY = "Technology"
    HEALTHCARE = "Healthcare"
    FINANCE = "Finance"
    EDUCATION = "Education" 
    MARKETING = "Marketing" 
    ENGINEERING = "Engineering"

class Careers(str, Enum):
    SOFTWARE_ENGINEER = "Software Engineer"
    DEVOPS_ENGINEER = "DevOps Engineer" 
    INFORMATION_SECURITY_ANALYST = "Information Security Analyst"
    DATA_SCIENTIST = "Data Scientist"
    DATA_ANALYST = "Data Analyst"
    DATABASE_ADMINISTRATOR = "Database Administrator"
    NETWORK_ENGINEER = "Network Engineer" 
    SYSTEMS_ENGINEER = "Systems Engineer" 
    HELP_DESK_TECH = "Help Desk Technician"
    SYSTEM_ADMINISTRATOR = "System Administrator" 

    REGISTERED_NURSE = "Registered Nurse" 
    PHYSICIAN = "Physician" 
    PHYSICIAN_ASSISTANT = "Physician Assistant"
    PSYCHOLOGIST = "Psychologist" 
    THERAPIST = "Therapist"
    COUNSELOR = "Counselor" 
    PHARMACIST = "Pharmacist" 
    MEDICAL_LABORATORY_TECHNICIAN = "Medical Laboratory Technician"
    PHARMACY_TECHNICIAN = "Pharmacy Technician" 

    INVESTMENT_BANKER = "Investment Banker" 
    FINANCIAL_ANALYST = "Financial Analyst" 
    BANK_TELLER = "Bank Teller" 
    ACCOUNTANT = "Accountant" 
    AUDITOR = "Auditor" 
    TAX_CONSULTANT = "Tax Consultant" 
    RISK_MANAGER = "Risk Manager" 
    BUDGET_ANALYST = "Budget Analyst"
    TREASURER = "Treasurer" 

    ELEMENTARY_TEACHER = "Elementary Teacher"
    HIGH_SCHOOL_TEACHER = "High School Teacher" 
    SPECIAL_EDUCATION_TEACHER = "Special Education Teacher" 
    PROFESSOR = "Professor"
    ACADEMIC_ADVISOR = "Academic Advisor" 
    DEAN = "Dean" 
    SCHOOL_PRINCIPAL = "School Principal"

    SEO_SPECIALIST  = "SEO Specialist"
    CONTENT_MARKETER = "Content Marketer" 
    SOCIAL_MEDIA_MANAGER = "Social Media Manager" 
    PR_SPECIALIST = "PR Specialist" 
    COMMUNICATIONS_DIRECTOR = "Communications Director" 
    MEDIA_BUYER = "Media Buyer" 
    COPYWRITER = "Copywriter" 
    GRAPHIC_DESIGNER = "Graphic Designer" 
    ART_DIRECTOR = "Art Director" 

    MECHANICAL_ENGINEER = "Mechanical Engineer"
    CIVIL_ENGINEER = "Civil Engineer" 
    INDUSTRIAL_ENGINEER = "Industrial Engineer" 
    AEROSPACE_ENGINEER = "Aerospace Engineer" 
    ELECTRICAL_ENGINEER = "Electrical Engineer" 
    NUCLEAR_ENGINEER = "Nuclear Engineer" 
    PLANT_MANAGER = "Plant Manager" 
    SUPPLY_CHAIN_ANALYST = "Supply Chain Analyst" 
    QUALITY_CONTROL_INSPECTOR = "Quality Control Inspector" 


class Skills(str, Enum): 
    DATA_ANALYSIS = "Data Analysis"
    SQL = "SQL"
    TABLEAU = "Tableau" 
    STATISTICAL_MODELING = "Statistical Modeling" 
    SOFTWARE_DEVELOPMENT = "Software Development" 
    CLOUD_COMPUTING = "Cloud Computing" 
    CYBERSECURITY = "Cybersecurity" 

    PATIENT_CARE = "Patient Care" 
    DIAGNOSTICS = "Diagnostics" 
    ELECTRONIC_HEALTH_RECORDS = "Electronic Health Records" 
    ANATOMY = "Anatomy"

    FINANCIAL_MODELING = "Financial Modeling" 
    TAX_ACCOUNTING = "Tax Accounting"
    AUDITING = "Auditing" 
    BUDGETING = "Budgeting" 

    SEO = "SEO" 
    CONTENT_WRITING = "Content Writing" 
    GRAPHIC_DESIGN = "Graphic Design"
    SOCIAL_MEDIA_MANAGEMENT = "Social Media Management"

    CURRICULUM_DESIGN = "Curriculum Design"
    CLASSROOM_MANAGEMENT = "Classroom Management" 
    LESSON_PLANNING = "Lesson Planning" 
    ED_TECH = "EdTech" 

    COMMUNICATION = "Communication" 
    LEADERSHIP = "Leadership" 
    PROBLEM_SOLVING = "Problem Solving"
    COLLABORATION = "Collaboration" 
    ADAPTABILITY = "Adaptability" 


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
    


