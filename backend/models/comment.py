from app import db
from models.base import BaseModel
from models.book import Book


class Comment(db.Model, BaseModel):

  __tablename__ = 'comments'

  content = db.Column(db.Text, nullable=False)

  book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
  book = db.relationship('Book', backref='comments')