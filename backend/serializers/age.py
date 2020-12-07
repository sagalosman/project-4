# from app import ma
# from serializers.base import BaseSchema
# from serializers.book import BookSchema
# # from serializers.user import UserSchema
# from marshmallow import fields
# from models.age import Age
# from models.user import User

# class AgeSchema(ma.SQLAlchemyAutoSchema, BaseSchema):

#   class Meta:
#     model = Age
#     load_instance = True
#     load_only = ('user_id',)

#   user_id = fields.Integer()

#   # books = fields.Nested('BookSchema', many=True)
#   user = fields.Nested('UserSchema', only =('id', 'username'))
  
  
  
