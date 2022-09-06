from time import time
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from core.config import Config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_hash(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_payload(token: str) -> dict:
    payload = jwt.decode(token, Config.SECRET_KEY,Config.ALGORITHM)
    return payload

def generate_jwt_token(payload: dict):
    c_payload = payload.copy()
    expired_time = datetime.utcnow() + timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
    c_payload.update({"token_type": "Bearer"})
    c_payload.update({"expired_at": str(expired_time)})

    jwt_token = jwt.encode(c_payload, Config.SECRET_KEY, algorithm=Config.ALGORITHM)

    return jwt_token