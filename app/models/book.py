# app/models/book.py
from pydantic import BaseModel

class Book(BaseModel):
    id: str
    name: str
    description: str
