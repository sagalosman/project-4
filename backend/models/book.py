from app import db
from models.base import BaseModel
from models.book_age import books_ages_join
from models.age import Age
from models.book_genre import books_genres_join
from models.genre import Genre

class Book(db.Model, BaseModel):

  __tablename__ = 'books'

  title = db.Column(db.String(40), nullable=False, unique=True)
  author = db.Column(db.String(40), nullable=False)
  description = db.Column(db.Text, nullable=False)
  image = db.Column(db.String(600), nullable=False, unique=True)

  ages = db.relationship('Age', secondary=books_ages_join, backref='books')
  genres = db.relationship('Genre', secondary=books_genres_join, backref='books')
