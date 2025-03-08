from app.db.schemas.category import CategoryCreate
from bson import ObjectId

async def create_category(db, category: CategoryCreate):
    new_category = {"name": category.name}
    result = await db["categories"].insert_one(new_category)
    new_category["_id"] = str(result.inserted_id)
    return new_category

async def get_all_category(db):
    categories = await db["categories"].find().to_list(length=None)
    for category in categories:
        category["_id"] = str(category["_id"])
    return categories

async def delete_category(db, category_id: str):
    result = await db["categories"].delete_one({"_id": ObjectId(category_id)})
    if result.deleted_count == 0:
        raise ValueError(f"Category with ID {category_id} not found")
    return {"message": f"Category with ID {category_id} deleted successfully"}

async def update_category_service(db, category_id: str, category_data: CategoryCreate):
    result = await db["categories"].update_one(
        {"_id": ObjectId(category_id)},
        {"$set": {"name": category_data.name}}
    )
    if result.matched_count == 0:
        raise ValueError(f"Category with ID {category_id} not found")
    updated_category = await db["categories"].find_one({"_id": ObjectId(category_id)})
    updated_category["_id"] = str(updated_category["_id"])
    return updated_category