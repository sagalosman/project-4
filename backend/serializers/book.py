from app import ma
from serializers.base import BaseSchema
from marshmallow import fields
from models.book import Book


class BookSchema(ma.SQLAlchemyAutoSchema, BaseSchema):

  class Meta:
    model = Book
    load_instance = True

  comments = fields.Nested('CommentSchema', many=True)