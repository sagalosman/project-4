from app import ma
from serializers.base import BaseSchema
from serializers.book import BookSchema
from marshmallow import fields
from models.genre import Genre


class PopulateGenreSchema(ma.SQLAlchemyAutoSchema, BaseSchema):

  class Meta:
    model = Genre
    load_instance = True

  books = fields.Nested('BookSchema', many=True)