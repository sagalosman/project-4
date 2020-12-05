from app import db
from models.base import BaseModel
from models.book import Book
from models.user import User


class Comment(db.Model, BaseModel):

  __tablename__ = 'comments'

  content = db.Column(db.Text, nullable=False)
  
  # ! This code in 1-M Relationships points to the ONE side
  book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
  book = db.relationship('Book', backref='comments')

  # ! This code in 1-M Relationships points to the ONE side
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  # Associate the 2 models together
  user = db.relationship('User', backref='comments')