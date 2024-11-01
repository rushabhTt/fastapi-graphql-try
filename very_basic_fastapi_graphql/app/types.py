# app/types.py
import strawberry
from sqlalchemy import Column, Integer, String
from .database import Base

# SQLAlchemy Model
class UserModel(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)

# GraphQL Type
@strawberry.type
class User:
    id: int
    name: str
    email: str