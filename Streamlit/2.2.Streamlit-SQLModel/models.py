from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship


class User(SQLModel, table=True):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    password: Optional[str]

    messages: list['Message'] = Relationship(back_populates='user')

class Message(SQLModel, table=True):
    __tablename__ = "messages"
    __table_args__ = {'extend_existing': True}
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    type: str
    user_id: int = Field(default=None, foreign_key='user.id')
    
    user: User = Relationship(back_populates='messages')