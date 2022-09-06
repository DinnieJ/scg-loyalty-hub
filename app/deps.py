from core.security.jwt.deps import JwtAuthentication
from fastapi import Depends
from app.user.repository import UserRepository

async def get_current_user(payload: dict = Depends(JwtAuthentication())):
    return await UserRepository.get_user(payload.get("username"))