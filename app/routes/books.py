# app/routes/books.py
from fastapi import APIRouter, Query
from typing import List
from app.models.book import Book
from app.database import books_db

router = APIRouter()

@router.get("/books", response_model=List[Book])
def get_books(sort_by: str = Query(None, description="Sort books by criteria")):
    if sort_by == "alphabetical":
        sorted_books = sorted(books_db, key=lambda x: x.name)
        return sorted_books
    return books_db
