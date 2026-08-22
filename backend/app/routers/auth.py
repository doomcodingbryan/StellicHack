# auth.py
# registration, login, me

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.models.models import User
from app.schemas.schemas import UserCreate, UserResponse, Token
from app.core.security import (
    hash_password, 
    verify_password,
    create_access_token,
)
from app.core.dependencies import(
    get_db, 
    get_current_user
)
from app.utils.enums import UserRole



router = APIRouter(
    prefix = "/auth", 
    tags = ["Authentication"]
)


@router.post("/register", response_model = UserResponse, status_code = status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user: 
        raise HTTPException(status_code = 400, detail = "Email already registered")

    if user.role == UserRole.ADMIN:
        raise HTTPException(
            status_code = 403, 
            detail = "Admin accounts cannot be self registered" 
        )
    
    user_data = user.model_dump()
    raw_password = user_data.pop("password") 
    hashed_password = hash_password(raw_password)


    # new_user = User(**user_data, password_hash = hashed_password, role=UserRole) # what to put for role? Since I have multiple alumn and student, putting placeholder for now
    new_user = User(**user_data, password_hash = hashed_password)

    try: 
        db.add(new_user)
        db.commit()

        db.refresh(new_user) 
    except Exception: 
        db.rollback()
        raise

    return new_user


@router.post("/login", response_model = Token, status_code = status.HTTP_200_OK)
def user_login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = (db.query(User).filter(User.email==form_data.username).first())

    if not user: 
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED, 
            detail = "Incorrect username or password", 
            headers = {"WWW-Authenticate": "Bearer"}, 
        )

    if not verify_password (form_data.password, user.password_hash): 
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED, 
            detail = "Incorrect username or password", 
            headers = {"WWW-Authenticate": "Bearer"}, 
        )

    token = create_access_token (
        {
            "sub": user.email
        }
    )

    return Token (access_token = token, token_type = "bearer") 


@router.get(
    "/me",
    response_model = UserResponse
)
def read_curent_user(
    current_user: User = Depends(get_current_user)
):
    return current_user