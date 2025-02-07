from sqlalchemy.orm import Session
from app.db.models.user import User
from app.db.models.category import Category
from app.db.schemas.user import UserCreate

# Service function to create a user
def create_user(db: Session, user: UserCreate):
    # Check if the category exists
    category = db.query(Category).filter(Category.id == user.category_id).first()
    if not category:
        raise ValueError(f"Category with ID {user.category_id} not found")

    # Create a new User instance
    db_user = User(
        name=user.name,
        email=user.email,
        nation_id=user.nation_id,
        file_code=user.file_code,
        category_id=user.category_id,
        register_date=user.register_date,
        promotion_date_III=user.promotion_date_III,
        promotion_date_II=user.promotion_date_II,
        promotion_date_I=user.promotion_date_I,
        gender= user.gender,
        address=user.address,
        date_of_birth = user.date_of_birth,
        Serial_number=user.Serial_number,
        W_OP =user.W_OP,
        place_of_transer = user.place_of_transer,
        date_of_transer =  user.date_of_transer


    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Service function to fetch all users
def get_all_users(db: Session):
    return db.query(User).all()

# Service function to fetch a user by nation_id
def get_user_by_nation_id(db: Session, nation_id: str):
    return db.query(User).filter(User.nation_id == nation_id).first()

def get_user_by_name(db: Session, name: str):
    return db.query(User).filter(User.name == name).first()

# Service function to get all users with a specific category_id (e.g., "Nurse")
def get_users_by_category_id(db: Session, category_id: int):
    # Fetch users with the specified category_id
    users = db.query(User).filter(User.category_id == category_id).all()
    return users

def get_user_by_gender(db: Session, gender: str):
    users = db.query(User).filter(User.gender == gender).all()  # Remove `.first()`
    return users

# Service function to update a user by ID
def update_user(db: Session, user_id: int, user_data: UserCreate):
    # Fetch the user to update
    db_user = db.query(User).filter(User.id == user_id).first()
    
    if not db_user:
        raise ValueError(f"User with ID {user_id} not found")
    
    # Check if the category exists
    category = db.query(Category).filter(Category.id == user_data.category_id).first()
    if not category:
        raise ValueError(f"Category with ID {user_data.category_id} not found")
    
    # Update the user's fields with the new data
    db_user.name=user_data.name,
    db_user.email=user_data.email,
    db_user.nation_id=user_data.nation_id,
    db_user.file_code=user_data.file_code,
    db_user.category_id=user_data.category_id,
    db_user.register_date=user_data.register_date,
    db_user.promotion_date_III=user_data.promotion_date_III,
    db_user.promotion_date_II=user_data.promotion_date_II,
    db_user.promotion_date_I=user_data.promotion_date_I,
    db_user.gender= user_data.gender,
    db_user.address=user_data.address,
    db_user.date_of_birth = user_data.date_of_birth,
    db_user.Serial_number=user_data.Serial_number,
    db_user.W_OP =user_data.W_OP,
    db_user.place_of_transer = user_data.place_of_transer,
    db_user.date_of_transer =  user_data.date_of_transer  

    # Commit the changes to the database
    db.commit()
    db.refresh(db_user)  # Refresh to get the updated instance

    return db_user

# Service function to delete a user by ID
def delete_user(db: Session, user_id: int):
    # Fetch the user to delete
    db_user = db.query(User).filter(User.id == user_id).first()
    
    if not db_user:
        raise ValueError(f"User with ID {user_id} not found")
    
    # Delete the user from the database
    db.delete(db_user)
    db.commit()

    return {"message": f"User with ID {user_id} deleted successfully"}

# Service function to get all users classified as "Nurses"
def get_nurses(db: Session):
    # Fetch the category ID for "Nurse"
    present_category = db.query(Category).filter(Category.name == "Present").first()
    
    if not present_category:
        raise ValueError("Category 'Nurse' not found")
    
    # Fetch users with category_id corresponding to "Nurse"
    present= db.query(User).filter(User.category_id == present_category.id).all()
    return present


