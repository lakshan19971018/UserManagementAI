import certifi
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

mongo_client = AsyncIOMotorClient(
    settings.DATABASE_URL,
    tls=True,
    tlsCAFile=certifi.where()
)
db = mongo_client["users"]
print("Connected successfully!")
async def get_db():
    try:
        yield db
    finally:
        pass  # motor auto-manages connection, explicit close ඕන නැහැ