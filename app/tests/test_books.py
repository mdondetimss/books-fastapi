# test/test_books.py
import pytest
from fastapi.testclient import TestClient
from app.main import app  # Importing the FastAPI app instance from app/main.py

client = TestClient(app)

def test_get_books_sort_by_alphabetical():
    response = client.get("/api/books?sort_by=alphabetical")
    assert response.status_code == 200
    books = response.json()
    assert len(books) > 0
    assert sorted(books, key=lambda x: x['name']) == books

def test_get_books_default():
    response = client.get("/api/books")
    assert response.status_code == 200
    books = response.json()
    assert len(books) > 0
