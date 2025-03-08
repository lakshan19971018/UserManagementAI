from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import users, categories, documents, admin, query

app = FastAPI(
    title="User Management System",
    description="API documentation for your FastAPI project.",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",  # ReDoc documentation
)

# Middleware for CORS (if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as per your environment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Routers
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(categories.router, prefix="/api/v1/categories", tags=["Categories"])
app.include_router(admin.router, prefix="/api/v1/admin", tags=["Admin"])
app.include_router(query.router, prefix="/api/v1/query", tags=["Query"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to your FastAPI application!"}