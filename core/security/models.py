from sqlalchemy.types import TypeDecorator, String
from passlib.context import CryptContext


class CryptPassword(TypeDecorator):
    impl = String

    def process_bind_param(self, value, dialect) -> str:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_context.hash(value)
