from fastapi import Depends , HTTPException
from sqlalchemy.orm import Session

from app.dependencies.auth import oauth2_scheme
from app.core.database import get_db
from app.core.security import decode_token
from app.models.user import User
from app.exceptions.costom_exceptions import (
    UserNotFoundException,
)

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    print("TOKEN RECEIVED:", token)

    user_id = decode_token(token)

    print("DECODED USER ID:", user_id)

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = db.query(User).filter(
        User.id == int(user_id)
    ).first()

    print("USER FOUND:", user)

    if user is None:
        raise UserNotFoundException()

    return user