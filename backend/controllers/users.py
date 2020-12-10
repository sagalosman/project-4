from flask import Blueprint, request, g, jsonify
from models.user import User
from models.book import Book
from serializers.user import UserSchema
from serializers.populate_user import PopulateUserSchema
from serializers.populate_book import PopulateBookSchema 
from middleware.secure_route import secure_route
from marshmallow import ValidationError


user_schema = UserSchema()
populate_user = PopulateUserSchema()

populate_book = PopulateBookSchema()

router = Blueprint(__name__, 'users')

# ! SIGNUP
@router.route('/signup', methods=['POST'])
def signup():
  request_body = request.get_json()
  user = user_schema.load(request_body)
  user.save()
  return user_schema.jsonify(user), 200

# ! LOGIN
@router.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  user = User.query.filter_by(email=data['email']).first()
  if not user:
    return { 'message': 'No user found with this email.' }, 200

  if not user.validate_password(data['password']):
    return { 'message': 'Unauthorized' }, 402

  token = user.generate_token()

  return { 'token': token, 'message': 'Nice to see you again' }


# ! GET ALL USER 
@router.route('/users', methods=['GET'])
def get_all_user():

  users = User.query.all()

  return user_schema.jsonify(users, many= True), 200


  # ! GET A SINGLE_USER by id
@router.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
  user = User.query.get(user_id)
  if not user:
    return { 'message': 'User not found!' }, 404
  return user_schema.jsonify(user), 200

# ! UPDATE USER by id

@router.route('/user/<int:user_id>', methods=['PUT'])
@secure_route
def update_user(user_id):

  existing_user = User.query.get(user_id)

  if not existing_user:
    return { 'message': 'User not found!' }, 404
  
    # ? Deserialization step
  try: 
    user = user_schema.load(
      request.get_json(),
      instance= existing_user,
      partial=True
    )

  
  except ValidationError as e:
    return { 'errors': e.messages, 'message': 'Something went wrong!'}

  if user !=g.current_user:
    return { 'message': 'Unauthorized' }, 401

  user.save()

  #  Serialization step

  return user_schema.jsonify(user), 200

# ! DELETE USER by id

@router.route('/user/<int:user_id>', methods=['DELETE'])
@secure_route
def remove_user(user_id):

  user = User.query.get(user_id)

  if not user:
    return { 'message': 'User not found!' }, 404
  
  if user != g.current_user:
    return { 'message': 'Unauthorized '}, 401

  user.remove()
  return { 'message': f'User {user_id} ---deleted successfully '}, 200



  # !  GET ALL BOOKS by user

@router.route('/user-books/<int:user_id>', methods=['GET'])
def get_all_books_by_user(user_id):

  user = User.query.get(user_id)

  if not user:
    return { 'message': 'User not found!' }, 404
  return populate_user.jsonify(user), 200

