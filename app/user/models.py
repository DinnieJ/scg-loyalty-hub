from core.db import Base, TimestampMixin
from core.security import CryptPassword
from typing import Optional
from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship


class User(Base, TimestampMixin):
    __tablename__ = "scg_users"

    id: Optional[int] = Column(BigInteger, primary_key=True)
    email: str = Column(String(100))
    name: str = Column(String(255))
    password: str = Column(CryptPassword)

    # posts = relationship("Post", cascade="all, delete", passive_deletes=True, back_populates="user")
