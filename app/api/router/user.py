from fastapi import APIRouter,Depends, HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import User
from app.core.security import hash_password, verify_password
from app.schemas.user import UserCreate,UserResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post(
    "/register",
    response_model = UserResponse,
    status_code=201
)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    existing_email = db.query(User).filter(User.email==user.email).first()
    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
     
    existing_username = db.query(User).filter(User.username==user.username).first()
    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already taken"
        )
    checked_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(checked_user)
    db.commit()
    db.refresh(checked_user)
    return checked_user