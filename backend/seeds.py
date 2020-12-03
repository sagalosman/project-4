
from app import app, db
from models.book import Book

with app.app_context():

  db.drop_all()
  db.create_all()

  cat_in_the_hat = Book(
    title= 'Cat in the hat',
    author= 'dr seuss',
    description= 'blah blah blah',
    image= 'https://cdn.waterstones.com/bookjackets/large/9780/0073/9780007348695.jpg'
  )

  charlie_and_the_chocolate_factory = Book(
    title= 'Charlie and the chocolate factory',
    author= 'Roald Dahl',
    description= 'description goes here',
    image= 'https://m.media-amazon.com/images/I/51gjXL3FldL.jpg'
  )

  charlottes_web = Book(
    title= 'Charlottes Web',
    author= 'E.B. White',
    description= 'This is a great book',
    image= 'tbc'
  )

  harry_potter_stone = Book (
    title= 'Harry Potter and the Philosophers Stone',
    author= 'J. K. Rowling',
    description= 'Scary!',
    image= '2'
  )

  db.session.add(cat_in_the_hat)
  db.session.add(charlie_and_the_chocolate_factory)
  db.session.add(charlottes_web)
  db.session.add(harry_potter_stone)
  db.session.commit()