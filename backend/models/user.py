from app import db, bcrypt
from models.base import BaseModel
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import *
from environment.config import secret

import jwt

class User(db.Model, BaseModel):

  __tablename__ = 'users'

  name = db.Column(db.String(75), nullable=False, unique=True)
  username = db.Column(db.String(15), nullable=False, unique=True)
  email = db.Column(db.String(128), nullable=False, unique=True)
  password_hash = db.Column(db.String(128), nullable=True)

  @hybrid_property
  def password(self):
    pass

  @password.setter
  def password(self, password_plaintext):
    self.password_hash = bcrypt.generate_password_hash(password_plaintext).decode('utf-8')


  def validate_password(self, password_plaintext):
    return bcrypt.check_password_hash(self.password_hash, password_plaintext)

  def generate_token(self):
    payload = {
      'exp': datetime.utcnow() + timedelta(days=1),
      'iat': datetime.utcnow(),
      'sub': self.id
    }
    
    token = jwt.encode(
      payload,
      secret,
      'HS256'
    ).decode('utf-8')

    return token