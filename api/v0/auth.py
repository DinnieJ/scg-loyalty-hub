from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_409_CONFLICT, HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED
from app.user import User, UserRepository
from app.user.schemas import UserRegisterSchema, CreateUserSuccessfulSchema, UserLoginSchema, UserToken
from app.deps import get_current_user
from core.security.jwt.utils import verify_hash, generate_jwt_token
from core.security.jwt.deps import JwtAuthentication


auth_router = APIRouter(
    prefix="/auth"
)


@auth_router.get("/", status_code=HTTP_200_OK)
async def auth_index():
    return {"Auth endpoint version": "0.0.0"}


@auth_router.post("/register", status_code=HTTP_201_CREATED, response_model=CreateUserSuccessfulSchema)
async def register(user: UserRegisterSchema):
    new_user = User(**user.dict())
    if await UserRepository.get_user(user.email) is not None:
        raise HTTPException(HTTP_409_CONFLICT, detail="User exists")
    else:
        await UserRepository.create(new_user)
    
    return new_user


@auth_router.post("/token", status_code=HTTP_200_OK, response_model=UserToken)
async def login(cred: UserLoginSchema):
    cred_user = await UserRepository.get_user(cred.email) 
    if cred_user is None:
        raise HTTPException(HTTP_404_NOT_FOUND, detail="User not found")
    elif verify_hash(cred.password, cred_user.password) is False:
        raise HTTPException(HTTP_401_UNAUTHORIZED, detail="Wrong username or password")
    else:
        token = generate_jwt_token({"username": cred_user.email})
        return {"token": token}


@auth_router.get("/me", status_code=HTTP_200_OK)
async def get_current_user(current_user: dict = Depends(get_current_user)):
    return current_user

