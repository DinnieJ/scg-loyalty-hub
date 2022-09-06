from sqlalchemy import select, insert

from core.db import get_session
from .models import User
from app.user.exceptions import UserExistException
from typing import Union

class UserRepository:
    async def create(user: User):
        async with get_session() as session:
            session.add(user)
            await session.commit()

    
    async def get_user(email: str) -> Union[User, None]:
        async with get_session() as session:
            check_user_query = select(User).where(User.email == email)
            result = await session.execute(check_user_query)
            return result.scalars().first()