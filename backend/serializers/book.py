from app import ma
from serializers.base import BaseSchema
from serializers.age import AgeSchema
from serializers.genre import GenreSchema
# from serializers.user import UserSchema
from marshmallow import fields
from models.book import Book


class BookSchema(ma.SQLAlchemyAutoSchema, BaseSchema):

  class Meta:
    model = Book
    load_instance = True

  comments = fields.Nested('CommentSchema', many=True)
  ages = fields.Nested('AgeSchema', many = True)
  genres = fields.Nested('GenreSchema', many = True)
  # users = fields.Nested('UserSchema', only =('id', 'username'))

