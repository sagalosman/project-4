from flask import Blueprint, request
from models.book import Book
from models.comment import Comment
from models.age import Age
# from models.genre import Genre
from serializers.book import BookSchema
from serializers.comment import CommentSchema
from serializers.age import AgeSchema
# from serializers.genre import GenreSchema 
from middleware.secure_route import secure_route


book_schema = BookSchema()

comment_schema = CommentSchema()


router = Blueprint(__name__, 'books')


# ! ROUTES FOR BOOKS

# GET all books
@router.route('/books', methods=['GET'])
def index():
  books = Book.query.all()

  return book_schema.jsonify(books, many=True), 200


# ! Delete The Books
# @router.route('/books/<int:id>', methods=['DELETE'])
# def remove(id):
#   book = Book.query.get(id)

#   book.remove()
#   return { 'message': f'Book {id}--deleted successfully' }
