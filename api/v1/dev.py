from fastapi import APIRouter, Header, Depends
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_403_FORBIDDEN

DEV_KEY = "thisisdevkey"


class VerifyDevEnv:
    def __init__(self) -> None:
        self.key = DEV_KEY
        pass

    def __call__(self, x_scg_dev: str = Header()) -> None:
        if x_scg_dev is None or x_scg_dev != self.key:
            raise HTTPException(status_code=HTTP_403_FORBIDDEN,
                                detail={"error": "You are unauthorized to use dev mode"})


dev_router = APIRouter(
    prefix="/dev",
    dependencies=[Depends(VerifyDevEnv())]
)


@dev_router.get("/")
async def dev_index():
    return {"message": "You are in dev router, this is available for developers only"}
