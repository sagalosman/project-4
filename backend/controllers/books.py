from flask import Blueprint, request, g
from models.book import Book
from models.comment import Comment
from models.genre import Genre
# from models.age import Age
from serializers.book import BookSchema
from serializers.populate_book import PopulateBookSchema
from serializers.comment import CommentSchema
from serializers.genre import GenreSchema 
# from serializers.age import AgeSchema
from serializers.populate_genre import PopulateGenreSchema
from middleware.secure_route import secure_route
from marshmallow import ValidationError



book_schema = BookSchema()
populate_book = PopulateBookSchema()

comment_schema = CommentSchema()

genre_schema = GenreSchema()
populate_genre = PopulateGenreSchema()

# age_schema = AgeSchema()



router = Blueprint(__name__, 'books')


# # ! ROUTES FOR AGE

# # GET ALL AGES
# @router.route('/ages', methods=['GET'])
# def all_age():
#   ages = Age.query.all()

#   return age_schema.jsonify(ages, many=True), 200

# # GET a single age
# @router.route('/ages/<int:id>', methods=['GET'])
# def get_single_age(id):
  
#   age = Age.query.get(id) 

#   if not age:
#     return { 'message': 'Age not found!' }, 404

#   return age_schema.jsonify(age), 200

#   # CREATE a Age 
# @router.route('/ages', methods=['POST'])
# def create_age():

#   age_dictionary = request.get_json()
#   print('CREATED THE AGE GROUP')
#   age_dictionary['user_id']= g.current_user.id
#   print('i have the ID')
#   try: 
#     age = age_schema.load(age_dictionary)
  
#   except ValidationError as e:
#     return { 'errors': e.messages, 'message': 'Something went wrong!'}
#   print('ABOUT TO SAVE')
#   age.save()
#   print('added to database')
#   return age_schema.jsonify(age), 200


# # DELETE a age
# @router.route('/ages/<int:id>', methods=['DELETE'])
# def remove_age(id):

#   age = Age.query.get(id)

#   if not age:
#     return { 'message': 'Age not found!' }, 404

#   age.remove()

#   return { 'message': f'Age {id} ---deleted successfully '}, 200


# ! ROUTES FOR BOOKS

# GET all books
@router.route('/books', methods=['GET'])
def index():
  books = Book.query.all()

  return book_schema.jsonify(books, many=True), 200

# GET a single book
@router.route('/books/<int:id>', methods=['GET'])
def get_single_book(id):
  
  book = Book.query.get(id) 

  if not book:
    return { 'message': 'Book not found!' }, 404

  return populate_book.jsonify(book), 200

# CREATE a book
@router.route('/books', methods=['POST'])
@secure_route
def create():
  book_dictionary = request.get_json()

  # This will provide the id of the current user posting the coffee
  book_dictionary['user_id']= g.current_user.id

  try: 
    book = populate_book.load(book_dictionary)
  
  except ValidationError as e:
    return { 'errors': e.messages, 'message': 'Something went wrong!'}
  
  book.save()

  return populate_book.jsonify(book), 200


# UPDATE a book
@router.route('/books/<int:id>', methods=['PUT'])
@secure_route
def update_book(id):
  existing_book = Book.query.get(id)

  if not existing_book:
    return { 'message': 'Book not found!!'}, 404

  # ? Deserialization step
  try: 
    book = populate_book.load(
      request.get_json(),
      instance= existing_book,
      partial=True
    )
  
  except ValidationError as e:
    return { 'errors': e.messages, 'message': 'Something went wrong!'}
  
  if book.user !=g.current_user:
    return { 'message': 'Unauthorized' }, 401

  book.save()


  # ? Serialization step
  return populate_book.jsonify(book), 200


# DELETE a book
@router.route('/books/<int:id>', methods=['DELETE'])
@secure_route
def remove(id):

  book = Book.query.get(id)

  if not book:
    return { 'message': 'Book not found!' }, 404
  
  if book.user != g.current_user:
    return { 'message': 'Unauthorized '}, 401

  book.remove()
  return { 'message': f'Book {id} ---deleted successfully '}, 200


# ! ROUTES FOR COMMENTS


#  GET single_comment associated with the book
@router.route('/books/<int:book_id>/comments/<int:comment_id>', methods=['GET'])
def get_single_comment(book_id, comment_id):
  
  comment = Comment.query.get(comment_id)
  
  if not comment:
    return { 'message': 'Comment not found!!!'}, 404

  book = Book.query.get(book_id)
  comment.book = book

  return comment_schema.jsonify(comment)


# Create a new comment 
@router.route('/books/<int:book_id>/comments', methods=['POST'])
@secure_route
def comment_create(book_id):
  
  comment_data = request.get_json()
  book = Book.query.get(book_id)
  
  # ? This link the comment with the user posting it
  comment_data['user_id'] = g.current_user.id

  # ? Deserialization step
  try: 
    comment = comment_schema.load(comment_data)
  
 
  except ValidationError as e:
    return { 'errors': e.messages, 'message': 'Something went wrong!' }

  comment.book = book
  comment.save()

   # ? Serialization step
  return comment_schema.jsonify(comment), 200


  #! # ###  UPDATE comments associated with a book  ####
  # @router.route('/books/<int:book_id>/comments/<int:comment_id>', methods=['PUT'])
 


  #! ####  DELETE comments associated with a book ####

  # @router.route('/books/<int:book_id>/comments/<int:comment_id>', methods=['DELETE'])
  # def get_comments(book_id):

  




# !  ROUTES FOR GENRES

# GET all genres

@router.route('/genres', methods=['GET'])
def get_genres():

  all_genres = Genre.query.all()

  return genre_schema.jsonify(all_genres, many=True), 200


 #  Get a single genre

@router.route('/genres/<int:genre_id>', methods=['GET'])
def get_single_genre(genre_id):

  genre = Genre.query.get(genre_id)

  if not genre:
    return { 'message': 'Genre not found!'}, 404

  return populate_genre.jsonify(genre), 200


# CREATE genre
@router.route('/genres', methods=['POST'])
@secure_route
def genre_create():

  genre_dictionary = request.get_json()


  genre_dictionary['user_id'] = g.current_user.id

  try:
    genre = genre_schema.load(genre_dictionary)
  
  except ValidationError as e:
    return { 'errors': e.messages, 'message': 'Something went wrong!' }

  genre.save()

  return populate_genre.jsonify(genre), 200

# CREATE BOOKS WITH genre and age_group
@router.route('/book-with-genres', methods=['POST'])
@secure_route
def create_book_with_genre():

  combined_dictionary = request.get_json()
  combined_dictionary['user_id'] = g.current_user.id

  try:
    book = populate_book.load(combined_dictionary)

  except ValidationError as e:
    return { 'errors': e.messages, 'message': 'Something went wrong!'}

  book.save()
  return populate_book.jsonify(book), 200

# UPDATE a genre

@router.route('/book-with-genres/<int:book_id>', methods=['PUT'])
@secure_route
def update_book_with_genre(book_id):
  existing_book = Book.query.get(book_id)

  if not existing_book:
    return {'message': 'Book not found!!'}, 404

  try:
     book = populate_book.load(
       request.get_json(),
       instance=existing_book,
       partial=True
     )

  except ValidationError as e:
    return {'errors': e.messages, 'message': 'Something went wrong!' }

  if book.user !=g.current_user:
    return {'message': 'Unauthorized' }, 401

  book.save()
  return populate_book.jsonify(book), 200






