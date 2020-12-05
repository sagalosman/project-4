
from flask import request, g
import jwt
from models.user import User
from environment.config import secret
from functools import wraps

def secure_route(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    raw_token = request.headers['Authorization']
    clean_token = raw_token.replace('Bearer ', '')

    try:
      payload = jwt.decode(clean_token, secret)
      user_id = payload['sub']
      user = User.query.get(user_id)

      if not user:
        return { 'message': 'Unauthorized' }, 401
      g.current_user = user
      
    except jwt.ExpiredSignatureError:
      return { 'message': 'Token has expired' }, 401

    except Exception as e:
      return { 'message': 'Unauthorized' }, 401

    return func(*args, **kwargs)

  return wrapper