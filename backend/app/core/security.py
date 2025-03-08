from jose import jwt, JWTError
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from app.core.config import settings
from datetime import datetime, timedelta
import asyncio

# Initialize OAuth2PasswordBearer for token extraction
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/admin/login")

# Initialize Passlib CryptContext for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hashes a plain-text password using bcrypt.
    :param password: The plain-text password.
    :return: The hashed password.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plain-text password against a hashed password.
    :param plain_password: The plain-text password.
    :param hashed_password: The hashed password.
    :return: True if the passwords match, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)

async def get_current_admin(token: str = Depends(oauth2_scheme)):
    """
    Decodes the JWT token to extract admin information asynchronously.
    :param token: The JWT token from the request.
    :return: The decoded payload if valid and role is admin.
    :raises HTTPException: If the token is invalid or role is not admin.
    """
    try:
        # Run synchronous jwt.decode in an executor to make it async-compatible
        loop = asyncio.get_event_loop()
        payload = await loop.run_in_executor(None, lambda: jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]))
        role = payload.get("role")
        if role != "admin":
            raise HTTPException(status_code=403, detail="Not authorized as admin")
        return payload
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid token")

def create_access_token(data: dict, expires_delta: timedelta = timedelta(hours=1)) -> str:
    """
    Creates a JWT token for the admin with a defined expiration time.
    :param data: The payload data to encode in the token.
    :param expires_delta: The expiration time delta for the token.
    :return: The encoded JWT token.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt