from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
import bcrypt
from pydantic import BaseModel
from sqlalchemy.orm import Session

from .database import get_db
from .models import User

router = APIRouter(prefix="/auth", tags=["auth"])


class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str
    language: str = "en"


class LoginRequest(BaseModel):
    email: str
    password: str


def user_response(user: User):
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role,
        "language": user.language,
        "createdAt": user.created_at.isoformat(),
    }


@router.post("/register")
def register(
    data: RegisterRequest,
    db: Session = Depends(get_db),
):
    email = data.email.lower().strip()

    existing = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="An account with this email already exists",
        )

    if len(data.password) < 6:
        raise HTTPException(
            status_code=400,
            detail="Password must be at least 6 characters",
        )

    user = User(
        name=data.name.strip(),
        email=email,
        password_hash=bcrypt.hashpw(
          data.password.encode("utf-8"),
          bcrypt.gensalt(),
        ).decode("utf-8"),

        role="user",
        language=data.language,
        created_at=datetime.utcnow(),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user_response(user)


@router.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db),
):
    email = data.email.lower().strip()

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user or not user.password_hash:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    
    if not bcrypt.checkpw(
      data.password.encode("utf-8"),
      user.password_hash.encode("utf-8"),
  ):

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    return user_response(user)


@router.get("/me")
def me():
    raise HTTPException(
        status_code=401,
        detail="Authentication token required",
    )

