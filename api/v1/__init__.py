from fastapi import APIRouter
from .dev import dev_router

v1_router = APIRouter()

v1_router.include_router(dev_router)
