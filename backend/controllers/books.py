from flask import Blueprint, request
from models.book import Book
from models.comment import Comment
from models.age import Age
from models.genre import Genre
from serializers.book import BookSchema
from serializers.comment import CommentSchema
from serializers.age import AgeSchema
from serializers.genre import GenreSchema 
from marshmallow import ValidationError



book_schema = BookSchema()

comment_schema = CommentSchema()


router = Blueprint(__name__, 'books')


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
    return { 'message': 'Book not found!' }

  return book_schema.jsonify(book), 200

# CREATE a book

@router.route('/books', methods=['POST'])
def create():
  book_dictionary = request.get_json()

  try: 
    book = book_schema.load(book_dictionary)
  
  except ValidationError as e:
    return { 'errors': e.messages, 'message': 'Something went wrong!'}
  
  book.save()

  return book_schema.jsonify(book), 200