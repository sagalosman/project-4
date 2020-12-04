from app import ma
from serializers.base import BaseSchema
from marshmallow import fields
from models.comment import Comment


class CommentSchema(ma.SQLAlchemyAutoSchema, BaseSchema):

  class Meta:
    model = Comment
    load_instance = True