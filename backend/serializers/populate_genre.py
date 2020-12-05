from app import ma
from serializers.base import BaseSchema
from serializers.book import BookSchema
from marshmallow import fields
from models.genre import Genre
from models.user import User

class PopulateGenreSchema(ma.SQLAlchemyAutoSchema, BaseSchema):

  class Meta:
    model = Genre
    load_instance = True
    load_only = ('user_id',)

  user_id = fields.Integer()

  books = fields.Nested('BookSchema', many=True)
  user = fields.Nested('UserSchema', only =('id', 'username'))