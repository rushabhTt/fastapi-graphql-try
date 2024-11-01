# app/schema.py
import strawberry

@strawberry.type
class Query:
    # Define a field named `hello` that returns a string message
    @strawberry.field
    def hello(self) -> str:
        return "Hello, GraphQL with FastAPI!"

# Create a GraphQL schema with the defined Query
schema = strawberry.Schema(query=Query)
