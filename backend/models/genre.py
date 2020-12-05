from app import db
from models.base import BaseModel
from models.user import User

class Genre(db.Model, BaseModel):

  __tablename__ = 'genres'

  genre = db.Column(db.String(40), unique=False, nullable=True)

  # ! This code in 1-M Relationships points to the ONE side
  # CREATE the actual column in the database
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
   # Associate the 2 models together
  user = db.relationship('User', backref='genres')

