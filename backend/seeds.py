
from app import app, db
from models.book import Book
from models.age import Age
from models.comment import Comment 

with app.app_context():

  db.drop_all()
  db.create_all()

  age_1 = Age(age='0-1')
  age_2 = Age(age='1-2')
  age_3 = Age(age='2-4')
  age_4 = Age(age='4-6')
  age_5 = Age(age='6-9')

  cat_in_the_hat = Book(
    title= 'Cat in the Hat',
    author= 'Dr Seuss',
    description= 'blah blah blah',
    image= 'https://cdn.waterstones.com/bookjackets/large/9780/0073/9780007348695.jpg',
    ages= [age_5]
  )

  charlie_and_the_chocolate_factory = Book(
    title= 'Charlie and the Chocolate Factory',
    author= 'Roald Dahl',
    description= 'description goes here',
    image= 'https://m.media-amazon.com/images/I/51gjXL3FldL.jpg',
    ages= [age_5]
  )

  charlottes_web = Book(
    title= 'Charlottes Web',
    author= 'E.B. White',
    description= 'This is a great book',
    image= 'tbc1'
  )

  harry_potter_stone = Book(
    title= 'Harry Potter and the Philosophers Stone',
    author= 'J. K. Rowling',
    description= 'Scary!',
    image= 'tbc2'
  )

  print('Books created')

  comment1 = Comment(
    content = 'This book is fun to read, My little ones love it',
    book=cat_in_the_hat
  )

  print('Comment created')
  
  print('Adding to database')

  db.session.add(cat_in_the_hat)
  db.session.add(charlie_and_the_chocolate_factory)
  db.session.add(charlottes_web)
  db.session.add(harry_potter_stone)
  db.session.add(age_5)
  db.session.commit()


  print('Completed')