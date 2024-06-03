from sqlmodel import SQLModel, Session, create_engine, select
from models import User, Message, Optional


# DATABASE_URL = 'sqlite:///database.db'
# DATABASE_URL = "postgresql://sina:ramze_sina@localhost:5432/database_sina"
DATABASE_URL = "postgresql://root:z8aCVH29rqcz4lQ85n2a7JHF@sina-postgre:5432/postgres"
engine = create_engine(DATABASE_URL)


def create_db_tables():
    SQLModel.metadata.create_all(engine)


def get_user_by_email(session: Session, email: str) -> Optional[User]:
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()


def create_user(name: str, email: str, password: str) -> Optional[User]:
    with Session(engine) as session:
        if get_user_by_email(session, email):
            return None
        user = User(name=name, email=email)
        user.set_password(password)
        session.add(user)
        session.commit()
        session.refresh(user)
    return user


def authenticate_user(email: str, password: str) -> Optional[User]:
    with Session(engine) as session:
        user = get_user_by_email(session, email)
        if user and user.verify_password(password):
            return user
    return None
