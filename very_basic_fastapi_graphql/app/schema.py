# app/schema.py
import strawberry
from .queries import Query
from .mutations import Mutation  # Import mutations

# Create a GraphQL schema with the defined Query
schema = strawberry.Schema(query=Query, mutation=Mutation)
