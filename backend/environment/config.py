import os

db_URI = os.getenv('DATABASE_URL', 'postgres://localhost:5432/books_db')
secret = os.getenv('SECRET', 'This is our secret book code')