
from app import app, db
from models.book import Book
# from models.age import Age
from models.comment import Comment 
from models.genre import Genre
from models.user import User


with app.app_context():

  db.drop_all()
  db.create_all()

  sagal = User(
    username="sagal",
    email="sagal@sagal.com",
    password="sagal"
  )
  admin = User(
    username= "admin",
    email="admin@admin.com",
    password="pass"
  )

  admin.save()
  sagal.save()

  print('Users created')


  # age_1 = Age(age='0-1')
  # age_2 = Age(age='1-2')
  # age_3 = Age(age='2-4')
  # age_4 = Age(age='4-6')
  # age_5 = Age(age='6-9')

  genre_1 = Genre(genre='Education')
  genre_2 = Genre(genre='Fiction')
  genre_3 = Genre(genre='Poetry')
  genre_4 = Genre(genre='Activity Book')
  genre_5 = Genre(genre='Fantasy')
  genre_6 = Genre(genre='Science Fiction')
  genre_7 = Genre(genre='Picture Book')

  print('Genres created!')

  cat_in_the_hat = Book(
    title= 'Cat in the Hat',
    author= 'Dr Seuss',
    description= 'The hat is in the cat',
    image= 'https://cdn.waterstones.com/bookjackets/large/9780/0073/9780007348695.jpg',
    # ages= [age_5],
    genres= [genre_2],
    user = admin
  )

  charlie_and_the_chocolate_factory = Book(
    title= 'Charlie and the Chocolate Factory',
    author= 'Roald Dahl',
    description= 'Mmmmm chocolate',
    image= 'https://m.media-amazon.com/images/I/51gjXL3FldL.jpg',
    # ages= [age_5],
    genres= [genre_2, genre_5],
    user= admin
  )

  charlottes_web = Book(
    title= 'Charlottes Web',
    author= 'E.B. White',
    description= 'I really got stuck into this one',
    image= 'tbc1',
    user = admin
  )

  harry_potter_stone = Book(
    title= 'Harry Potter and the Philosophers Stone',
    author= 'J. K. Rowling',
    description= 'Scary!',
    image= 'tbc2',
    genres= [genre_2],
    user = admin
  )

  the_tiger_came_to_tea = Book(
    title= 'The Tiger Who Came To Tea',
    author= 'Judith Kerr',
    description= 'His favourite was Rooibos!',
    image= 'tbc3',
    # ages= [age_3],
    genres= [genre_2, genre_7],
    user = admin   
  )

 
  the_gruffalo = Book(
    title= 'The Gruffalo',
    author= 'Julia Donaldson',
    description= 'A rhyming story about a mouse and a monster',
    image= 'tbc4',
    # ages= [age_3],
    genres= [genre_2, genre_5, genre_7],
    user = admin    
  )

  the_hungry_caterpillar = Book(
    title= 'The Very Hungry Caterpillar',
    author= 'Eric Carle',
    description= 'Soooooo hungry!',
    image= 'tbc5',
    # ages= [age_3],
    genres= [genre_2, genre_5, genre_7],
    user = admin   
  )

  twits = Book(
    title= 'The Twits',
    author= 'Roald Dahl',
    description= 'They really are twits',
    image= 'tbc6',
    # ages= [age_5],
    genres= [genre_2],
    user = admin    
  )

  codename_bananas = Book(
    title= 'Codename Bananas',
    author= 'David Walliams',
    description= 'Double-O bananas',
    image= 'tbc7',
    # ages= [age_5],
    genres= [genre_2],
    user = admin    
  )

  stick_man = Book(
    title= 'Stick Man',
    author= 'Julia Donaldson',
    description= 'Surprisingly scary!',
    image= 'tbc8',
    # ages= [age_5],
    genres= [genre_2, genre_5],
    user = admin    
  )


  print('Books created')

  comment1 = Comment(
    content = 'This book is fun to read, My little ones love it',
    book=cat_in_the_hat,
    user = admin
  )

  print('Comment created') 
  print('Adding to database')


  db.session.add(cat_in_the_hat)
  db.session.add(charlie_and_the_chocolate_factory)
  db.session.add(charlottes_web)
  db.session.add(harry_potter_stone)
  db.session.add(the_tiger_came_to_tea)
  db.session.add(the_gruffalo)
  db.session.add(comment1)
  # db.session.add(age_1)
  # db.session.add(age_2)
  # db.session.add(age_3)
  # db.session.add(age_4)
  # db.session.add(age_5)
  db.session.add(genre_1)
  db.session.add(genre_2)
  db.session.add(genre_3)
  db.session.add(genre_4)
  db.session.add(genre_5)
  db.session.add(genre_6)
  db.session.add(genre_7)
  db.session.commit()


  print('Completed')



