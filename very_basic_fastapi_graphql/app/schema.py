# app/schema.py
import strawberry
from .types import User  # Import the custom User type
from .data import user_data  # Import the simulated data

@strawberry.type
class Query:
    # Define a field named `hello` that returns a string message
    @strawberry.field
    def hello(self) -> str:
        return "Hello, GraphQL with FastAPI!"

    # Define a query to return a hardcoded user
    @strawberry.field
    def get_user(self) -> User:
        return User(id=1, name="Alice", email="alice@example.com")

    # Add new get_user_by_id field
    @strawberry.field
    def get_user_by_id(self, id: int) -> User:
        # The next() function takes this generator expression as an argument.
        return next((user for user in user_data if user.id == id), None)
        
        # You can rewrite this using a traditional loop:
        # for user in user_data:
        #     if user.id == id:
        #         return user
        # return None
    
    # Add new all_users field
    @strawberry.field
    def all_users(self) -> list[User]:
        return user_data

# Create a GraphQL schema with the defined Query
schema = strawberry.Schema(query=Query)
