from app.db.models.admin import Admin
from app.core.security import hash_password
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

def create_admin(db: Session, email: str, password: str):
    try:
        hashed_password = hash_password(password)
        new_admin = Admin(
            email=email,
            hashed_password=hashed_password,
        )
        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)
        return new_admin
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
