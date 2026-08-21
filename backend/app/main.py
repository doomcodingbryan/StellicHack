# main.py

from fastapi import FastAPI 
from app.routers import auth
from app.core.database import engine, Base
import app.models.models

Base.metadata.create_all(bind = engine)

app = FastAPI( title = "StellicHack Pathfinder")


# @app.get("/")