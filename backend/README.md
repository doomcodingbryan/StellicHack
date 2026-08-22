# Pathfinder Backend

This directory contains the backend/API for the **StellicHack Pathfinder**. 

---

# Backend Startup

cp .env.example .env

docker compose build

docker compose up -d 

docker compose ps

docker compose exec backend-api python -m app.seed.seed_data

curl http://localhost:8080/

Open: 
http://localhost:8080/docs


Starts psql and fastapi backend at localhost:8080 --> 
docker compose up --build 

Run the container detached --> 
docker compose up --build -d

Check running containers: 
docker compose ps

hackathon_postgres and hackathon_backend should be up 

Logs: docker compose logs
Backend logs only: docker compose logs backend-api
Follow backend logs: docker compose logs -f backend-api
Follow PSQL logs: docker compose logs -f postgres-db

Stop Backend: 
docker compose down

Reset the database: 
docker compose down -v 
NOTE: deletes psql docker volume/database data

Rebuild: 
docker compose up --build

FastAPI Documentation using Swagger: 
http://localhost:8080/docs

Development seed data: 
Stored in: app/seed/seed_data.py



---

# Tech Stack
- Python 3.11 
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- bcrypt
- Docker

---

# Backend Responsibilities

- User registration and authentication 
- JWT authentication
- Student profiles
- Institutions
- Degrees
- Courses
- Skills
- Student skills
- Career skill requirements
- Career matching
- Skill gap analysis
- Alumni and Student matching
- Student projects
- Career pathway generation 
- PostgeSQL database access
- API validation

---

# Backend File Structure

```text
backend
├── app
│   ├── core
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   ├── __init__.py
│   │   └── security.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   └── models.py
│   ├── routers
│   │   ├── auth.py
│   │   ├── careers.py
│   │   ├── courses.py
│   │   ├── degrees.py
│   │   ├── __init__.py
│   │   ├── institutions.py
│   │   ├── pathways.py
│   │   ├── projects.py
│   │   ├── recommendations.py
│   │   ├── skills.py
│   │   └── students.py
│   ├── schemas
│   │   ├── __init__.py
│   │   └── schemas.py
│   ├── seed
│   │   └── seed_data.py
│   ├── services
│   │   ├── career_service.py
│   │   ├── course_service.py
│   │   ├── degree_service.py
│   │   ├── gap_analysis_service.py
│   │   ├── matching_service.py
│   │   ├── pathway_service.py
│   │   ├── project_service.py
│   │   ├── recommendation_service.py
│   │   └── student_service.py
│   └── utils
│       ├── enums.py
│       └── __init__.py
├── Dockerfile
├── README.md
└── requirements.txt
```

