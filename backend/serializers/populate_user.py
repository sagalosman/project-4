from app import ma
from serializers.base import BaseSchema
from serializers.book import BookSchema
from serializers.comment import CommentSchema
from models.user import User
from marshmallow import fields

class PopulateUserSchema(ma.SQLAlchemyAutoSchema, BaseSchema):

  class Meta:
    model = User
    load_instance = True
    exclude = ('password_hash',)
    load_only = ('email', 'password')

  password = fields.String(required=True)

  books = fields.Nested('BookSchema', many=True)
  comments = fields.Nested('CommentSchema', many=True)