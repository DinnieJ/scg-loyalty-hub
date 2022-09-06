from sqlalchemy import select, delete, update

from core.db import get_session
from .models import Post
from typing import Union

class PostRepository:
    async def create(post: Post):
        async with get_session() as session:
            session.add(post)
            await session.commit()
        
        return post


    async def delete(id: int) -> bool:
        async with get_session() as session:
            try:
                query = delete(Post).where(Post.id == id)
                await session.execute(query)
                await session.commit()
                return True
            except Exception:
                return False


    async def update(id, data) -> bool:
        async with get_session() as session:
            try:
                query = update(Post).where(Post.id == id).values(**data)
                await session.execute(query)
                await session.commit()
                return True
            except Exception:
                return False


    
    async def get_post_by_id(id) -> Union[Post, None]:
        async with get_session() as session:
            check_user_query = select(Post).where(Post.id == id)
            result = await session.execute(check_user_query)
            return result.scalars().first()


    
    async def is_post_belong_to_user(user_id: int, post_id: int) -> bool:
        async with get_session() as session:
            query = select(Post).where(Post.user_id == user_id).where(Post.id == post_id)
            result = await session.execute(query)
            return False if result.scalars().first() is not None else True

