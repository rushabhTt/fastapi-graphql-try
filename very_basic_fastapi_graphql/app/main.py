# app/main.py
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from .schema import schema  # Import the schema from schema.py
from .database import engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI()

# Set up a GraphQL router with the defined schema
graphql_app = GraphQLRouter(schema)

# Add the GraphQL route to the FastAPI app with a /graphql endpoint
app.include_router(graphql_app, prefix="/graphql")

# Optional: Add a health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)