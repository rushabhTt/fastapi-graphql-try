# app/data.py
from .types import User

# Simulate a database with a hardcoded list of users
user_data = [
    User(id=1, name="Alice", email="alice@example.com"),
    User(id=2, name="Bob", email="bob@example.com"),
    User(id=3, name="Charlie", email="charlie@example.com")
]