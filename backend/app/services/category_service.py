from sqlalchemy.orm import Session
from app.db.models.category import Category
from app.db.schemas.category import CategoryCreate

# Service function to create a new category
def create_category(db: Session, category: CategoryCreate):
    # Create a new Category instance using the name provided in category object
    db_category = Category(
        name=category.name
    )
    
    db.add(db_category)
    db.commit()
    db.refresh(db_category)  # Make sure the created category is refreshed with data
    
    return db_category  # Ensure this is returning the created db_category

#Show all category

def get_all_category(db:Session):
    return db.query(Category).all()

#delete category
def delete_category(db:Session,category_id:int):
    db_category = db.query(Category).filter(Category.id==category_id).first()

    if not db_category:
        raise ValueError(f"Category with ID {category_id} not found")
    db.delete(db_category)
    db.commit()

    return {"message": f"Category with ID {category_id} deleted successfully"}

#edit category

def update_category_service(db: Session, category_id: int, category_data: CategoryCreate):
    db_category = db.query(Category).filter(Category.id == category_id).first()

    if not db_category:
        raise ValueError(f"Category with ID {category_id} not found")
    
    db_category.name = category_data.name
    db.commit()
    db.refresh(db_category)  # Refresh to get the updated instance

    return db_category




