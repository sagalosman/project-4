from app import db
from models.base import BaseModel
from models.book import Book
from models.user import User


class Age(db.Model, BaseModel):

  __tablename__ = 'ages'

  cont