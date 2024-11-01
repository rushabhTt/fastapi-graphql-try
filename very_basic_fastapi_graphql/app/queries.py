# app/queries.py
import strawberry
from typing import List
from .types import User
from .database import SessionLocal
from .types import UserModel

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello, GraphQL with FastAPI!"

    @strawberry.field
    def get_user_by_id(self, id: int) -> User:
        db = SessionLocal()
        try:
            db_user = db.query(UserModel).filter(UserModel.id == id).first()
            if db_user:
                return User(id=db_user.id, name=db_user.name, email=db_user.email)
            return None
        finally:
            db.close()
    
    @strawberry.field
    def all_users(self) -> List[User]:
        db = SessionLocal()
        try:
            users = db.query(UserModel).all()
            return [User(id=u.id, name=u.name, email=u.email) for u in users]
        finally:
            db.close()