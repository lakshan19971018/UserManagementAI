from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.schemas.category import CategoryCreate, CategoryResponse
from app.services.category_service import create_category,get_all_category,delete_category,update_category_service
from app.db.session import get_db
from typing import List

router = APIRouter()

@router.post('/category', response_model=CategoryResponse)
async def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    try:
        #Call the service function to create a category
        new_category = create_category(db=db, category=category)
        return new_category  # Return the new category, this will be validated by the response model
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))




#get all category
@router.get("/all-categories", response_model=List[CategoryResponse])
async def get_all_categories(db: Session = Depends(get_db)):
    try:
        #Fetch all categories from the service function
        categories = get_all_category(db=db)
        if not categories:
            raise HTTPException(status_code=404, detail="No categories found")
        return categories
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

#delete category
@router.delete("/{category_id}", response_model=dict)
async def delete_existing_category(category_id: int, db: Session = Depends(get_db)):
    try:
        #Using the service function to delete the user by ID
        response = delete_category(db=db, category_id=category_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



@router.put("/{category_id}", response_model=CategoryResponse)
async def update_category(category_id: int, category: CategoryCreate, db: Session = Depends(get_db)):
    try:
        updated_category = update_category_service(db=db, category_id=category_id, category_data=category)
        return updated_category
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while updating the category.")
