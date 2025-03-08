# import certifi
# from motor.motor_asyncio import AsyncIOMotorClient
# import asyncio

# async def test_connection():
#     DATABASE_URL = "mongodb+srv://lakshan200:ABCDEf45@cluster0.ijlzf.mongodb.net/user?retryWrites=true&w=majority"
#     try:
#         client = AsyncIOMotorClient(
#             DATABASE_URL,
#             tls=True,
#             tlsCAFile=certifi.where()
#         )
#         db = client["users"]  # Connection string එකේ "user" තිබුණත්, "users" access කරමු
#         #await db["test_collection"].insert_one({"test": "connection"})
#         print("Connected successfully and inserted data!")
#     except Exception as e:
#         print(f"Connection failed: {e}")
#     finally:
#         client.close()

# if __name__ == "__main__":
#     asyncio.run(test_connection())

from pymongo import MongoClient

client = MongoClient("mongodb+srv://lakshan200:ABCDEf45@cluster0.ijlzf.mongodb.net/user?retryWrites=true&w=majority")
db = client["db1"]
collection = db["youtube"]
document = {"name":"Lakshan"}
insert_doc = collection.insert_one(document=document)
client.close()