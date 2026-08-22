# main.py

from fastapi import FastAPI 
from app.routers import(
    auth, 
    careers,
    courses,
    degrees,
    institutions, 
    projects, 
    skills, 
    students, 
    recommendations,
    pathways
)
from app.core.database import engine, Base
import app.models.models


Base.metadata.create_all(bind = engine)

app = FastAPI( title = "StellicHack Pathfinder")

app.include_router(auth.router)
app.include_router(careers.router)
app.include_router(courses.router)
app.include_router(degrees.router)
app.include_router(institutions.router)
app.include_router(projects.router)
app.include_router(skills.router)
app.include_router(students.router)
app.include_router(recommendations.router)
app.include_router(pathways.router) 

@app.get("/")
def root(): 
    return {
        "message": "StellicHack Pathfinder API", 
        "status": "running"
    }
