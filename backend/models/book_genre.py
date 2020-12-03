from app import db

books_genres_join = db.Table('books_genres',
  db.Column('genres_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True),
  db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True)
)