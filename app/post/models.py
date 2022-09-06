from core.db import Base, TimestampMixin
from core.security import CryptPassword
from typing import Optional
from sqlalchemy import Column, BigInteger, String, Text, ForeignKey
from sqlalchemy.orm import relationship


class Post(Base, TimestampMixin):
    __tablename__ = "scg_posts"

    id: Optional[int] = Column(BigInteger, primary_key=True)
    title: str = Column(String(255))
    content: str = Column(Text)

    user_id = Column(BigInteger,ForeignKey("scg_users.id"), nullable=False)
    user = relationship("User", backref="scg_posts")