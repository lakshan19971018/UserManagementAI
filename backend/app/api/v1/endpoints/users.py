# routers/user_router.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user, get_all_users,get_user_by_nation_id,update_user,delete_user,get_users_by_category_id,get_user_by_gender,get_user_by_name
from app.db.session import get_db
from typing import List


router = APIRouter()

@router.post("/users/", response_model=UserResponse)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = create_user(db=db, user=user)
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/all-users",response_model=List[UserResponse])
async def fetch_all_users(db: Session = Depends(get_db)):
    try:
        # Call service function to get all users
        users = get_all_users(db=db)
        if not users:
            raise HTTPException(status_code=404, detail="No users found")
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/nation_id/{nation_id}", response_model=UserResponse)
async def fetch_user_by_nation_id(nation_id: str, db: Session = Depends(get_db)):
    try:
        # Call service function to get user by nation_id
        user = get_user_by_nation_id(db=db, nation_id=nation_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/name/{name}", response_model=UserResponse)
async def fetch_user_by_name(name: str, db: Session = Depends(get_db)):
    try:
        # Call service function to get user by name
        user = get_user_by_name(db=db, name=name)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.put("/{user_id}", response_model=UserResponse)
async def update_user_details(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    try:
        # Using the service function to update an existing user
        updated_user = update_user(db=db, user_id=user_id, user_data=user)
        return updated_user
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while updating the user.")


@router.delete("/{user_id}", response_model=dict)
async def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    try:
        # Using the service function to delete the user by ID
        response = delete_user(db=db, user_id=user_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.get("/category/{category_id}", response_model=list[UserResponse])
async def get_users_by_category(category_id: int, db: Session = Depends(get_db)):
    try:
        # Using the service function to get users by category_id
        users = get_users_by_category_id(db=db, category_id=category_id)
        return users
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.get("/{gender}", response_model=list[UserResponse])
async def get_users_by_gender(gender: str, db: Session = Depends(get_db)):
    try:
        # Call the service function to get users by gender
        users = get_user_by_gender(db=db, gender=gender)
        return users
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))