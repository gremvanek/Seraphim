from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from .models import User
from .database import get_db
from .dependencies import oauth2_scheme


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.token == token).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user
