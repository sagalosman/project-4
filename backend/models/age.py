from app import db
from models.base import BaseModel

class Age(db.Model, BaseModel):

  __tablename__ = 'ages'

  age = db.Column(db.String(10), unique=True, nullable=True)

