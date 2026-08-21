Creating a backend: 
Tech Stack
Python, FastAPI, SQLAlchemy ORM

To start off here is what the file structure should look like: 

project/

|- backend/
|    |- app/
|    |   |- main.py
|    |   |- database.py
|    |   |- models/
|    |   |- schemas/
|    |   |- routers/
|    |   |- services/
|    |   |- auth/ 
|    |   |- core/ 
|    |- requirements.txt
|    |- README.md   
|    |- Dockerfile
|    |- tests/
|    |- alembic/
|    |- .dockerignore
|    |- .venv
|- docker-compose.yml
|- .env

Create the venv using: 
python3 -m venv .venv

run: 
source .venv/bin/activate


install:
fastapi - pip install fastapi[standard]
uvicorn - pip install uvicorn
sqlalchemy - pip install sqlalchemy
psycopg2 - pip install psycopg2-binary
pydantic - pip install pydantic
pydantic-settings - pip install pydantic-settings
pip install "python-jose[cryptography]" "passlib[bcrypt]"


DOCKER COMPOSE: 
run the container - docker compose up --build
run in background (detached) - docker compose up -d 
stop everything - docker compose down 
stop and reset - docker compose down -v

Locations and setups for docker files here are pretty much universal for python backends 



All files and stuff will probably need a revision and improvements once they get working a bit

Everything still needs work, just didn't want the repo to be empty
