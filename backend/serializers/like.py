from app import ma
from serializers.base import BaseSchema
from marshmallow import fields
from models.like import Like
from models.user import User


class LikeSchema(ma.SQLAlchemyAutoSchema, BaseSchema):

  class Meta:
    model = Like
    load_instance = True

    load_only = ('user_id',)

  user_id = fields.Integer()

  user = fields.Nested('UserSchema', only=('id', 'username'))