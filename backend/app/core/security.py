from datetime import datetime, timedelta
from typing import Optional
import hashlib

from jose import jwt
from passlib.context import CryptContext
from cryptography.fernet import Fernet

from app.core.config import settings


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def _prehash(password: str) -> str:
    """
    Pre-hash password to avoid bcrypt 72-byte limitation
    """
    return hashlib.sha256(password.encode()).hexdigest()

def hash_password(password: str) -> str:
    return pwd_context.hash(_prehash(password))

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(_prehash(plain_password), hashed_password)



ALGORITHM = "HS256"


def create_access_token(
    data: dict,
    expires_delta: Optional[timedelta] = None
) -> str:
    to_encode = data.copy()

    expire = datetime.utcnow() + (
        expires_delta
        if expires_delta
        else timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=ALGORITHM,
    )

    return encoded_jwt


if not settings.ENCRYPTION_KEY:
    raise RuntimeError("ENCRYPTION_KEY environment variable is not set")


fernet = Fernet(settings.ENCRYPTION_KEY)


def encrypt_value(value: str) -> bytes:
    """
    Encrypt a string value and return raw bytes suitable for BYTEA columns.
    """
    return fernet.encrypt(value.encode())


def decrypt_value(value: bytes) -> str:
    """
    Decrypt raw BYTEA bytes from the database back into a string.
    """
    return fernet.decrypt(value).decode()
