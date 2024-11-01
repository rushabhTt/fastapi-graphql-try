# app/schema.py
import strawberry
from .types import User  # Import the custom User type

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

# Create a GraphQL schema with the defined Query
schema = strawberry.Schema(query=Query)
