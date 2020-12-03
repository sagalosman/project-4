from app import db
from models.base import BaseModel

class Book(db.Model, BaseModel):

  __tablename__ = 'books'

  title = db.Column(db.String(40), nullable=False, unique=True)
  author = db.Column(db.String(40), nullable=False)
  description = db.Column(db.Text, nullable=False)
  image = db.Column(db.String(600), nullable=False, unique=True)

