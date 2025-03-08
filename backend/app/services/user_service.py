from app.db.schemas.user import UserCreate
from bson import ObjectId

async def create_user(db, user: UserCreate):
    category = await db["categories"].find_one({"_id": user.category_id})
    if not category:
        raise ValueError(f"Category with ID {user.category_id} not found")
    
    # datetime.date objects ISO format string එකකට convert කරනවා
    new_user = {
        "name": user.name,
        "email": user.email,
        "nation_id": user.nation_id,
        "file_code": user.file_code,
        "category_id": user.category_id,
        "register_date": user.register_date.isoformat() if user.register_date else None,
        "promotion_date_III": user.promotion_date_III.isoformat() if user.promotion_date_III else None,
        "promotion_date_II": user.promotion_date_II.isoformat() if user.promotion_date_II else None,
        "promotion_date_I": user.promotion_date_I.isoformat() if user.promotion_date_I else None,
        "gender": user.gender,
        "address": user.address,
        "date_of_birth": user.date_of_birth.isoformat() if user.date_of_birth else None,
        "serial_number": user.serial_number,
        "w_op": user.w_op,
        "place_of_transfer": user.place_of_transfer,
        "date_of_transfer": user.date_of_transfer.isoformat() if user.date_of_transfer else None
    }
    result = await db["users"].insert_one(new_user)
    new_user["_id"] = str(result.inserted_id)
    return new_user

async def get_all_users(db):
    users = await db["users"].find().to_list(length=None)
    for user in users:
        user["_id"] = str(user["_id"])
    return users

async def get_user_by_nation_id(db, nation_id: str):
    user = await db["users"].find_one({"nation_id": nation_id})
    if user:
        user["_id"] = str(user["_id"])
    return user

async def get_user_by_id(db, user_id: str):
    user = await db["users"].find_one({"_id": ObjectId(user_id)})  # User ID එක ObjectId එකක්
    if user:
        user["_id"] = str(user["_id"])
    return user

async def get_user_by_file_code(db, file_code: str):
    user = await db["users"].find_one({"file_code": file_code})
    if user:
        user["_id"] = str(user["_id"])
    return user

async def get_user_by_serial_number(db, serial_number: int):
    user = await db["users"].find_one({"serial_number": serial_number})
    if user:
        user["_id"] = str(user["_id"])
    return user

async def get_user_by_name(db, name: str):
    user = await db["users"].find_one({"name": name})
    if user:
        user["_id"] = str(user["_id"])
    return user

async def get_users_by_category_id(db, category_id: str):
    # category_id එක string එකක් ලෙසම use කරනවා
    users = await db["users"].find({"category_id": category_id}).to_list(length=None)
    for user in users:
        user["_id"] = str(user["_id"])
    return users

async def get_user_by_gender(db, gender: str):
    users = await db["users"].find({"gender": gender}).to_list(length=None)
    for user in users:
        user["_id"] = str(user["_id"])
    return users

async def update_user(db, user_id: str, user_data: UserCreate):
    category = await db["categories"].find_one({"_id": user_data.category_id})
    if not category:
        raise ValueError(f"Category with ID {user_data.category_id} not found")
    result = await db["users"].update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {
            "name": user_data.name,
            "email": user_data.email,
            "nation_id": user_data.nation_id,
            "file_code": user_data.file_code,
            "category_id": user_data.category_id,
            "register_date": user_data.register_date.isoformat() if user_data.register_date else None,
            "promotion_date_III": user_data.promotion_date_III.isoformat() if user_data.promotion_date_III else None,
            "promotion_date_II": user_data.promotion_date_II.isoformat() if user_data.promotion_date_II else None,
            "promotion_date_I": user_data.promotion_date_I.isoformat() if user_data.promotion_date_I else None,
            "gender": user_data.gender,
            "address": user_data.address,
            "date_of_birth": user_data.date_of_birth.isoformat() if user_data.date_of_birth else None,
            "serial_number": user_data.serial_number,
            "w_op": user_data.w_op,
            "place_of_transfer": user_data.place_of_transfer,
            "date_of_transfer": user_data.date_of_transfer.isoformat() if user_data.date_of_transfer else None
        }}
    )
    if result.matched_count == 0:
        raise ValueError(f"User with ID {user_id} not found")
    updated_user = await db["users"].find_one({"_id": ObjectId(user_id)})
    updated_user["_id"] = str(updated_user["_id"])
    return updated_user

async def delete_user(db, user_id: str):
    result = await db["users"].delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0:
        raise ValueError(f"User with ID {user_id} not found")
    return {"message": f"User with ID {user_id} deleted successfully"}

async def get_nurses(db):
    # "Present" category එකේ id එක "1" ලෙස assume කරනවා
    category = await db["categories"].find_one({"_id": "1"})
    if not category:
        raise ValueError("Category 'Present' (ID: '1') not found")
    users = await db["users"].find({"category_id": "1"}).to_list(length=None)
    for user in users:
        user["_id"] = str(user["_id"])
    return users