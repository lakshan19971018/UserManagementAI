from fastapi import APIRouter, HTTPException, Depends
from app.db.schemas.category import CategoryCreate, CategoryResponse
from app.services.category_service import create_category, get_all_category, delete_category, update_category_service
from app.db.session import get_db
from typing import List

router = APIRouter()

@router.post('/category', response_model=CategoryResponse)
async def create_new_category(category: CategoryCreate, db=Depends(get_db)):
    try:
        new_category = await create_category(db=db, category=category)
        return new_category
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/all-categories", response_model=List[CategoryResponse])
async def get_all_categories(db=Depends(get_db)):
    try:
        categories = await get_all_category(db=db)
        if not categories:
            raise HTTPException(status_code=404, detail="No categories found")
        return categories
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{category_id}", response_model=dict)
async def delete_existing_category(category_id: str, db=Depends(get_db)):
    try:
        response = await delete_category(db=db, category_id=category_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{category_id}", response_model=CategoryResponse)
async def update_category(category_id: str, category: CategoryCreate, db=Depends(get_db)):
    try:
        updated_category = await update_category_service(db=db, category_id=category_id, category_data=category)
        return updated_category
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while updating the category.")