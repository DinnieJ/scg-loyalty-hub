from app.deps import get_current_user
from fastapi import Depends
from .repository import PostRepository
from fastapi.responses import JSONResponse

async def is_post_belong_to_user(id: int, current_user = Depends(get_current_user)):
    if await PostRepository.is_post_belong_to_user(current_user.id, id):
        return JSONResponse(status_code=401, content={"message": "You are not allowed to make change to this record"})