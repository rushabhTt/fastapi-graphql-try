# app/main.py
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from .schema import schema  # Import the schema from schema.py

# Initialize the FastAPI app
app = FastAPI()

# Set up a GraphQL router with the defined schema
graphql_app = GraphQLRouter(schema)

# Add the GraphQL route to the FastAPI app with a /graphql endpoint
app.include_router(graphql_app, prefix="/graphql")
