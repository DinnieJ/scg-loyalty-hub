from fastapi import APIRouter
from .v1 import v1_router
from .v0 import v0_router

root_router = APIRouter()

root_router.include_router(v1_router, prefix="/v1")
root_router.include_router(v0_router, prefix="/alpha")
