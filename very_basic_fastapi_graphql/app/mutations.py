# app/mutations.py
import strawberry
from .types import User, UserModel
from .database import SessionLocal

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, email: str) -> User:
        db = SessionLocal()
        try:
            db_user = UserModel(name=name, email=email)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return User(id=db_user.id, name=db_user.name, email=db_user.email)
        finally:
            db.close()