from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.db.models.admin import Admin
from app.db.schemas.admin import AdminLogin, AdminTokenResponse,AdminCreate,AdminResponse
from app.core.security import verify_password, create_access_token
from app.db.session import get_db
from app.services.admin_service import create_admin


router = APIRouter()

@router.post("/login", response_model=AdminTokenResponse)
def login_admin(admin_data: AdminLogin, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.email == admin_data.email).first()
    if not admin or not verify_password(admin_data.password, admin.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
        )
    # Create a JWT token for the admin
    token = create_access_token({"sub": admin.email, "role": "admin"})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/admins/", response_model=AdminResponse)
async def create_new_admin(admin: AdminCreate, db: Session = Depends(get_db)):
    try:
        new_admin = create_admin(db=db, email=admin.email, password=admin.password)
        return AdminResponse(id=new_admin.id, email=new_admin.email)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
