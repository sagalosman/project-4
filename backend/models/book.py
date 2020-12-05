from app import db
from models.base import BaseModel
from models.book_genre import books_genres_join
from models.genre import Genre
from models.user import User

class Book(db.Model, BaseModel):

  __tablename__ = 'books'

  title = db.Column(db.String(40), nullable=False, unique=True)
  author = db.Column(db.String(40), nullable=False)
  description = db.Column(db.Text, nullable=False)
  image = db.Column(db.String(600), nullable=True, unique=True)


  # ! This code in M-M Relationships
  genres = db.relationship('Genre', secondary=books_genres_join, backref='books')

  # ! This code in 1-M Relationships points to the ONE side
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  user = db.relationship('User', backref='books')
