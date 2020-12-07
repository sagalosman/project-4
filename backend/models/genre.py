from app import db
from models.base import BaseModel


class Genre(db.Model, BaseModel):

  __tablename__ = 'genres'

  genre = db.Column(db.String(40), unique=False, nullable=True)