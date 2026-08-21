# dependencies.py 
# holds reusable dependencies: get_db(), get_current_user()...

from typing import Generator
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from app.models.models import User
from app.core.security import verify_access_token


# defining get_db to start sessions for routes when needed
def get_db():

    # start a session with the database
    db = SessionLocal()

    try: 
        yield db
    # use finally for cleanup regardless of error thrown or success
    finally:
        db.close()


# swagger needs the endpoint to send the user and pass
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "/auth/login")


def get_current_user( token: str = Depends(oauth2_scheme), db: Session = Depends(get_db),) -> User: 
    payload = verify_access_token(token) 

    if payload is None: 
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED, 
            detail = "Invalid authentication credentials", 
            # from oauth2 spec
            headers = {"WWW-Authenticate": "Bearer"}
        )

    email = payload.get("sub")
    if email is None: 
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail= "Invalid authentication credentials", 
            headers = {"WWW-Authenticate": "Bearer"}
        )

    user = (
        db.query(User).filter(User.email == email).first()
    )

    if user is None: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail = "Invlaid authentication credentials", 
            headers = {"WWW-Authenticate": "Bearer"}
        )

    # return user so other routes can utilize
    return user



# dependency factory, returns another function (role checker in this case) that FastAPI can use as a dependency
# def require_roles ( allowed_roles: list[UserRole]):
#     def role_checker(
#         current_user: User = Depends(get_current_user)
#     ):
#         if current_user.role not in allowed_roles:
#             raise HTTPException(
#                 status_code = status.HTTP_403_FORBIDDEN, 
#                 detail = "Insufficient permissions"
#             )
        
#         return current_user
    
#     return role_checker
