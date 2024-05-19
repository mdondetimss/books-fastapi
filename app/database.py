# app/database.py
from typing import List
from app.models.book import Book

books_db: List[Book] = [
    Book(id="1", name="Algebra Basics", description="Learn the basics of algebra."),
    Book(id="2", name="Calculus 101", description="An introduction to calculus."),
    Book(id="3", name="Data Structures", description="Fundamentals of data structures."),
]
