from fastapi import APIRouter, Depends
from app.deps import get_current_user
from app.post.repository import PostRepository
from app.post.models import Post
from app.post.schemas import PostSchema, UpdatePostSchema
from app.post.deps import is_post_belong_to_user
from starlette.responses import JSONResponse

post_router = APIRouter(
    prefix="/post"
)


@post_router.get("/")
async def get_all():
    pass

@post_router.get("/{id}", status_code=200)
async def get(id: int):
    post = await PostRepository.get_post_by_id(id)
    if post is None:
        return JSONResponse(status_code=404, content={"message": "Post not found"})
    else: 
        return post

@post_router.post("/", status_code=201)
async def insert(body: PostSchema, current_user = Depends(get_current_user)):
    new_post = Post(**body.dict(), user_id=current_user.id)
    return await PostRepository.create(new_post)

@post_router.patch("/{id}", dependencies=[Depends(is_post_belong_to_user)])
async def update(id: int, body: UpdatePostSchema):
    return await PostRepository.update(id, body.dict())

@post_router.delete("/{id}", dependencies=[Depends(is_post_belong_to_user)])
async def remove(id: int):
    return await PostRepository.delete(id)