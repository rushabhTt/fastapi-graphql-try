# app/types.py
import strawberry

# Define a GraphQL User type
@strawberry.type
class User:
    id: int
    name: str
    email: str
