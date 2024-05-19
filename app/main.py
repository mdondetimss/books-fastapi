# app/main.py
from fastapi import FastAPI
from app.routes import books

app = FastAPI()

app.include_router(books.router, prefix="/api")
