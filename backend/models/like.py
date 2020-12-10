from app import db
from models.base import BaseModel
from models.book import Book
from models.user import User


class Like(db.Model, BaseModel):

  __tablename__ = 'likes'

  like = db.Column(db.Integer, nullable=True)
  
  # ! This code in 1-M Relationships points to the ONE side
  book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)

  book = db.relationship('Book', backref='likes')

  # ! This code in 1-M Relationships points to the ONE side
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  # Associate the 2 models together
  user = db.relationship('User', backref='likes')