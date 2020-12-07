from app import ma
from serializers.base import BaseSchema
from marshmallow import fields
from models.book import Book
from models.user import User


class BookSchema(ma.SQLAlchemyAutoSchema, BaseSchema):

  class Meta:
    model = Book
    load_instance = True

    load_only = ('user_id',)

  user_id = fields.Integer()
  user = fields.Nested('UserSchema', only=('id', 'username'))

