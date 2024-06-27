from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    hashed_password: str

    messages: List['Message'] = Relationship(back_populates='user')

    def set_password(self, password: str):
        self.hashed_password = pwd_context.hash(password)

    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.hashed_password)


class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    type: str
    user_id: int = Field(default=None, foreign_key='user.id')

    user: User = Relationship(back_populates='messages')
