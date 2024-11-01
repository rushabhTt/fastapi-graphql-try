# app/mutations.py
import strawberry
from .types import User
from .data import user_data  # Import the user list

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, email: str) -> User:
        # Create a new user with the next available ID
        new_user = User(id=len(user_data) + 1, name=name, email=email)
        user_data.append(new_user)
        return new_user
