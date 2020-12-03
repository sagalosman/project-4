from app import db

books_ages_join = db.Table('books_ages',
  db.Column('age_id', db.Integer, db.ForeignKey('ages.id'), primary_key=True),
  db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True)
)