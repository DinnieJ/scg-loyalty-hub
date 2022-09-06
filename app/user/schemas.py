from lib2to3.pytree import Base
from pydantic import BaseModel, EmailStr, Field, validator
from re import match


class UserRegisterSchema(BaseModel):
    email: str = EmailStr()
    name: str = Field(max_length=255)
    password: str = Field(max_length=64)

    @validator('password')
    def password_format(cls, v):
        if not match("^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]+)$", v):
            raise ValueError("Password must be alphanumeric")
        return v

    class Config:
        orm_mode = True


class CreateUserSuccessfulSchema(BaseModel):
    email: str
    name: str
    
    class Config:
        orm_mode = True

class UserLoginSchema(BaseModel):
    email: str = EmailStr()
    password: str = Field(max_length=64)

class UserToken(BaseModel):
    token: str
