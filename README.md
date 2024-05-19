# Books FastAPI Application Lab

This lab guides you through creating a simple FastAPI application with a structured project layout, including models, routes, and tests. The example includes endpoints for retrieving and sorting books.

## 1.Project Structure
```python
my-books-fastapi/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── models/
│ │ ├── init.py
│ │ └── book.py
│ ├── routes/
│ │ ├── init.py
│ │ └── books.py
│ ├── database.py
├── test/
│ ├── init.py
│ └── test_books.py


```
## 2.Setting Up the Project.
```python

from pydantic import BaseModel
app/__init__.py
app/models/book.py
```
## 3.Define the book model here.
```python

from pydantic import BaseModel
class Book(BaseModel):
    id: str
    name: str
    description: str
```

## 3.Define the routes here.

```python

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
```
## 5 Define the books endpoint, including sorting functionality.
```python
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
```
## 6 Simute Db with sample data.
```python
# app/database.py
from typing import List
from app.models.book import Book

books_db: List[Book] = [
    Book(id="1", name="Algebra Basics", description="Learn the basics of algebra."),
    Book(id="2", name="Calculus 101", description="An introduction to calculus."),
    Book(id="3", name="Data Structures", description="Fundamentals of data structures."),
]
```
# 7.Initialize the FastAPI app and include the books router.
```python
from fastapi import FastAPI
from app.routes import books

app = FastAPI()

app.include_router(books.router, prefix="/api")

from fastapi import FastAPI
from app.routes import books

app = FastAPI()

app.include_router(books.router, prefix="/api")
```

## 8.This file indicates that the test directory is a Python package
```python
from fastapi import FastAPI
test/__init__.py
```
## 9.Write tests for the /books endpoint, including sorting functionality.
```python
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
```
## 10.Run Test
```python
from fastapi import FastAPI
pytest test/
```





