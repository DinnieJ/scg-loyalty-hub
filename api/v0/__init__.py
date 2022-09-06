from fastapi import APIRouter
from .auth import auth_router
from .post import post_router

v0_router = APIRouter()

v0_router.include_router(auth_router)
v0_router.include_router(post_router)
