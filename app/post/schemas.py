from pydantic import BaseModel, Field
from typing import Optional

class PostSchema(BaseModel):
    title: str = Field(max_length=100)
    content: str = Field(max_length=999)

class UpdatePostSchema(PostSchema):
    title: Optional[str] = Field(max_length=100)
    content: Optional[str] = Field(max_length=999)