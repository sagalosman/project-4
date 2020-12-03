from flask import Blueprint, request
from models.book import Book
from models.comment import Comment
from models.age import Age
# from models.genre import Genre
from serializers.book import BookSchema
from serializers.comment import CommentSchema
from serializers.age import AgeSchema
# from serializers.genre import GenreSchema 



book_schema = BookSchema()

comment_schema = CommentSchema()


router = Blueprint(__name__, 'books')


# ! ROUTES FOR BOOKS

# GET all books
@router.route('/books', methods=['GET'])
def index():
  books = Book.query.all()

  return book_schema.jsonify(books, many=True), 200
