# database.py

# import for the engine to actually start up the db 
from sqlalchemy import create_engine 
# import to create sessions with the db 
from sqlalchemy.orm import sessionmaker
# used for sqlalchemy to let it know that the class is actually a db table instead of a regular class
from sqlalchemy.orm import declarative_base
# import config
from config import settings

# initialize engine to create connections when needed
engine = create_engine(settings.DATABASE_URL) 

# blueprint to create sessions in the future using db = SessionLocal()
SessionLocal = sessionmaker(
    autocommit = False, 
    autoflush = False, 
    bind = engine
)

Base = declarative_base()