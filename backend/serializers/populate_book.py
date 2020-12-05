from app import ma
from serializers.base import BaseSchema
from serializers.genre import GenreSchema
from serializers.user import UserSchema
from serializers.comment import CommentSchema
from marshmallow import fields
from models.book import Book


class PopulateBookSchema(ma.SQLAlchemyAutoSchema, BaseSchema):

  class Meta:
    model = Book
    load_instance = True


  comments = fields.Nested('CommentSchema', many=True)
  genres = fields.Nested('GenreSchema', many = True)
  user = fields.Nested('UserSchema', only =('id', 'username'))

