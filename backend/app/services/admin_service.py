from app.core.security import hash_password
from fastapi import HTTPException, status
from bson import ObjectId

async def create_admin(db, email: str, password: str):
    try:
        hashed_password = hash_password(password)
        new_admin = {
            "email": email,
            "hashed_password": hashed_password
        }
        result = await db["admins"].insert_one(new_admin)
        new_admin["_id"] = str(result.inserted_id)  # Convert ObjectId to string
        return new_admin
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )