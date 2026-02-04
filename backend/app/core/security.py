from passlib.context import CryptContext
from cryptography.fernet import Fernet
from app.core.config import settings
pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)

fernet = Fernet(settings.ENCRYPTION_KEY.encode())

def hash_password(password: str) -> str:
    """
    Secure password hashing using PBKDF2 (no 72-byte limit, no native deps).
    """
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)


def encrypt_value(value: str) -> bytes:
    return fernet.encrypt(value.encode("utf-8"))


def decrypt_value(value: bytes) -> str:
    return fernet.decrypt(value).decode("utf-8")
