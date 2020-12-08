
from app import app, db
from models.book import Book
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




  print('Age groups created!')

  genre_1 = Genre(genre='Education')
  genre_2 = Genre(genre='Fiction')
  genre_3 = Genre(genre='Poetry')
  genre_4 = Genre(genre='Activity Book')
  genre_5 = Genre(genre='Fantasy')
  genre_6 = Genre(genre='Science Fiction')
  genre_7 = Genre(genre='Picture Book')


  print('Genres created!')

  tracy_beaker = Book(
    title= 'Starring Tracy Beaker',
    author= 'Jacqueline Wilson',
    description= 'Tracy is a orphan who lives in a Childrens Home which she calls in her point of view "The Dumping Ground". She plans on becoming an actress just like her Hollywood mum, and she plans to make a start with this great opportunity. She desperately wants her mum to come and watch her acting Scrooge.',
    image= 'https://d3ddkgxe55ca6c.cloudfront.net/assets/t1497975559/a/c3/44/113562-ml-53622.jpg',
    age= '10-16',
    genres= [genre_2],
    user = admin
  )
  hetty_feather = Book(
    title= 'Hetty Feather',
    author= 'Jacqueline Wilson',
    description= 'The book is about a girl named Hetty Feather who goes through a hard childhood. Hetty is abandoned by her mother as a newborn baby and is left at the Foundling Hospital. Hetty is given to a foster family and returns to the Foundling Hospital when she is six years old.',
    image= 'https://m.media-amazon.com/images/I/61dz70uSzEL.jpg',
    age= '10-16',
    genres= [genre_2],
    user = admin
  )
  tracy_beaker2 = Book(
    title= 'The Story of Tracy Beaker',
    author= 'Jacqueline Wilson',
    description= 'Tracy Beaker is a funny, imaginative and articulate ten-year-old girl, but she can also be angry, impulsive and a bit violent too. Tracy lives in a childrens home but constantly hopes that her absent, glamorous mum will come and take her away. One day Cam visits the home, to write a piece on the children.',
    image= 'https://images-na.ssl-images-amazon.com/images/I/91mPKwML6iL.jpg',
    age= '10-16',
    genres= [genre_2],
    user = admin
  )
  double_act = Book(
    title= 'Double Act',
    author= 'Jacqueline Wilson',
    description= 'The book takes the form of the twins alternately narrating the story of their life in an Accounts book. Ruby and Garnet are ten-year-old identical twins living with their father and grandmother since their mother, Opal, died.',
    image= 'https://images-na.ssl-images-amazon.com/images/I/91XbgXzN9FL.jpg',
    age= '10-16',
    genres= [genre_2],
    user = admin
  )
  best_friends = Book(
    title= 'Best Friends',
    author= 'Jacqueline Wilson',
    description= 'Gemma and Alice have known each other all their lives, but when Gemma reads Alices diary at a sleepover, it eventually leads her to discover Alice is moving. Because of their distance, Gemma and Alice struggle to stay friends, with the possibility of each other making new friends.',
    image= 'https://images-na.ssl-images-amazon.com/images/I/51EBX1KP9WL.jpg',
    age= '8-10',
    genres= [genre_2],
    user = admin
  )

  cat_in_the_hat = Book(
    title= 'Cat in the Hat',
    author= 'Dr Seuss',
    description= 'The Cat in the Hat is a book where an eccentric stranger visits two children, Sally and Sam, who are home alone and having a very dull day. Their mother is out, and when the Cat comes in, he reassures the kids that their mother wont mind him or his tricks!',
    image= 'https://cdn.waterstones.com/bookjackets/large/9780/0073/9780007348695.jpg',
    age= '6-9',
    genres= [genre_2],
    user = admin
  )
  green_eggs_and_ham = Book(
    title= 'Green Eggs and Ham',
    author= 'Dr Seuss',
    description= 'Green Eggs and Ham is a much-loved classic by Dr. Seuss, which is not only fun to read but also raises important questions about the relationship between beliefs and experiences. Sam-I-Am spends the entire book offering green eggs and ham to the narrator, who adamantly refuses to try the delicacy because he does not like Sam-I-Am. Sam-I-Am offers to serve the dish in a number of different locations with a number of different partners. However, his persistence does not succeed until the very end, when the narrator finally caves in and tries it, only to find he loves it, and will eat it anywhere and with anyone. He also overcomes his dislike for Sam-I-Am.',
    image= 'https://images-na.ssl-images-amazon.com/images/I/51Q7ZVHDFlL.jpg',
    age= '6-9',
    genres= [genre_2],
    user = admin
  )
  how_the_grinch_stole_christmas = Book(
    title= 'How the Grinch Stole Christmas!',
    author= 'Dr Seuss',
    description= 'The Grinch, a grouchy, cave-dwelling creature, hates Christmas; his only companion is his unloved but loyal dog, Max. ... From his cave, the Grinch can hear the noisy Christmas festivities that take place in Whoville. Continually annoyed, he devises a wicked scheme to steal their presents, trees, and Christmas food.',
    image= 'https://images-na.ssl-images-amazon.com/images/I/81SJew0hSOL.jpg',
    age= '6-9',
    genres= [genre_2],
    user = admin
  )
  one_fish_two_fish = Book(
    title= 'One fish, two fish, red fish, blue fish',
    author= 'Dr Seuss',
    description= 'One Fish Two Fish Red Fish Blue Fish is a 1960 childrens book by Dr. Seuss (Theodor Seuss Geisel). A simple rhyming book for learner readers, it is a book with a freewheeling plot about a boy and a girl, and the many amazing creatures they have for friends and pets. One Fish Two Fish Red Fish Blue Fish was part of the Beginner Book Video series which included Oh, the Thinks You Can Think! and The Foot Book.',
    image= 'https://images-na.ssl-images-amazon.com/images/I/81Cnh7MuzTL.jpg',
    age= '6-9',
    genres= [genre_2],
    user = admin
  )
  oh_the_places_you_will_go = Book(
    title= 'Oh, the Places You Will Go!',
    author= 'Dr Seuss',
    description= 'Oh, the Places Youll Go! is a book written and illustrated by childrens author Dr. Seuss. It was first published by Random House on January 22, 1990. It was his last book to be published during his lifetime. The book concerns the journey of life and its challenges.',
    image= 'https://images-na.ssl-images-amazon.com/images/I/51HY300joCL._SX364_BO1,204,203,200_.jpg',
    age= '6-9',
    genres= [genre_2],
    user = admin
  )
  fox_in_socks = Book(
    title= 'Fox in Socks',
    author= 'Dr Seuss',
    description= 'Fox in Socks is a childrens book by Dr. Seuss, first published in 1965. It features two main characters, Fox (an anthropomorphic fox) who speaks almost entirely in densely rhyming tongue-twisters and Knox (a yellow anthropomorphic character) who has a hard time following up Foxs tongue-twisters until the end.',
    image= 'https://images-eu.ssl-images-amazon.com/images/I/51g2xGyFCkL._AC_UL600_SR429,600_.jpg',
    age= '6-9',
    genres= [genre_2],
    user = admin
  )
  the_lorex = Book(
    title= 'The Lorax',
    author= 'Dr Seuss',
    description= 'Twelve-year-old Ted lives in a place virtually devoid of nature; no flowers or trees grow in the town of Thneedville. Ted would very much like to win the heart of Audrey, the girl of his dreams, but to do this, he must find that which she most desires: a Truffula tree. To get it, Ted delves into the story of the Lorax, once the gruff guardian of the forest, and the Once-ler, who let greed overtake his respect for nature.',
    image= 'https://images-na.ssl-images-amazon.com/images/I/51rKfxKi+bL._SX362_BO1,204,203,200_.jpg',
    age= '6-9',
    genres= [genre_2],
    user = admin
  )
  horton_hears_a_who = Book(
    title= 'Horton Hears a Who!',
    author= 'Dr Seuss',
    description= 'elephant Horton finds a speck of dust floating in the Jungle of Nool. Upon investigation of the speck, Horton discovers the tiny city of Who-ville and its residents, the Whos, which he can hear but cannot see. Horton forms a friendship with the mayor of Who-ville, Ned McDodd, and promises to transport Who-ville to safety. However, Horton encounters opposition from his jungle neighbors, who dont want to believe in the existence of Who-ville.',
    image= 'https://cdn.waterstones.com/bookjackets/large/9780/0074/9780007455942.jpg',
    age= '6-9',
    genres= [genre_2],
    user = admin
  )
  hop_on_pop = Book(
    title= 'Hop on Pop',
    author= 'Dr Seuss',
    description= 'As the tagline states this is “The Simplest Seuss for the Youngest Use.” On each page there are a few words in full caps. This highlights what words are important. These words are then used in a short simple sentence on the same page so children can see how they’re used. ',
    image= 'https://images-na.ssl-images-amazon.com/images/I/5138vQtt2TL._SX354_BO1,204,203,200_.jpg',
    age= '1-3',
    genres= [genre_2],
    user = admin
  )

  abc = Book(
    title= 'Dr. Seuss ABC',
    author= 'Dr Seuss',
    description= 'Dr. Seuss ABC is a 1963 childrens A to Z alphabetical picture book by Dr. Seuss. It was published as part of the Random House Beginner Books series. It contains several short poems about a variety of characters, and is designed to introduce basic alphabet book concepts to children. ',
    image= 'https://cdn.waterstones.com/bookjackets/large/9780/0074/9780007487752.jpg',
    age= '1-3',
    genres= [genre_2],
    user = admin
  )

  charlie_and_the_chocolate_factory = Book(
    title= 'Charlie and the Chocolate Factory',
    author= 'Roald Dahl',
    description= ' A young boy wins a tour through the most magnificent chocolate factory in the world, led by the worlds most unusual candy maker. When Willy Wonka decides to let five children into his chocolate factory, he decides to release five golden tickets in five separate chocolate bars, causing complete mayhem.',
    image= 'https://m.media-amazon.com/images/I/51gjXL3FldL.jpg',
    age= '6-9',
    genres= [genre_2, genre_5],
    user= admin
  )
  matilda = Book(
    title= 'Matilda',
    author= 'Roald Dahl',
    description= 'Roald Dahl work tells the story of Matilda, a gifted girl forced to put up with a crude, distant father and mother. Worse, Agatha Trunchbull, the evil principal at Matildas school, is a terrifyingly strict bully. However, when Matilda realizes she has the power of telekinesis, she begins to defend her friends from Trunchbulls wrath and fight back against her unkind parents.',
    image= 'https://images-na.ssl-images-amazon.com/images/I/919-lhp2zeL.jpg',
    age= '6-9',
    genres= [genre_2, genre_5],
    user= admin
  )
  giant_peach = Book(
    title= 'James and the Giant Peach',
    author= 'Roald Dahl',
    description= 'Roald Dahls beloved childrens tale follows the adventures of James, an orphaned young British boy. Forced to live with his cruel aunts, James finds a way out of his bleak existence when he discovers an enormous enchanted peach. After rolling into the sea inside the buoyant fruit, James, accompanied by a crew of friendly talking insects, sets sail for New York City.',
    image= 'https://images-na.ssl-images-amazon.com/images/I/81PPxXWNA2L.jpg',
    age= '6-9',
    genres= [genre_2, genre_5],
    user= admin
  )
  the_bfg = Book(
    title= 'The BFG',
    author= 'Roald Dahl',
    description= 'Ten-year-old Sophie is in for the adventure of a lifetime when she meets the Big Friendly Giant. Naturally scared at first, the young girl soon realizes that the 24-foot behemoth is actually quite gentle and charming. As their friendship grows, Sophies presence attracts the unwanted attention of Bloodbottler, Fleshlumpeater and other giants. After traveling to London, Sophie and the BFG must convince Queen Victoria to help them get rid of all the bad giants once and for all.',
    image= 'https://images-na.ssl-images-amazon.com/images/I/91I2ywLs1YL.jpg',
    age= '6-9',
    genres= [genre_2, genre_5],
    user= admin
  )
  the_witches = Book(
    title= 'The Witches',
    author= 'Roald Dahl',
    description= 'While staying at a hotel in England with his grandmother, Helga, young Luke inadvertently spies on a convention of witches. The Grand High Witch reveals a plan to turn all children into mice through a magical formula. When they find that Luke has overheard, the witches test the formula on him. Now, with the help of Helga and the hotel manager, Mr. Stringer, Luke the mouse must fight back against the witches.',
    image= 'https://images-na.ssl-images-amazon.com/images/I/71Bbi-tg-mL.jpg',
    age= '6-9',
    genres= [genre_2, genre_5],
    user= admin
  )
  fantastic_mr_fox = Book(
    title= 'Fantastic Mr Fox',
    author= 'Roald Dahl',
    description= 'After 12 years of bucolic bliss, Mr. Fox breaks a promise to his wife (Meryl Streep) and raids the farms of their human neighbors, Boggis, Bunce and Bean. Giving in to his animal instincts endangers not only his marriage but also the lives of his family and their animal friends. When the farmers force Mr. Fox and company deep underground, he has to resort to his natural craftiness to rise above the opposition.',
    image= 'https://images-na.ssl-images-amazon.com/images/I/81JPnO7wUBL.jpg',
    age= '6-9',
    genres= [genre_2, genre_5],
    user= admin
  )
  georges_marvellous_medicine = Book(
    title= 'Georges Marvellous Medicine',
    author= 'Roald Dahl',
    description= 'Georges Marvellous Medicine is a childrens book written by Roald Dahl and illustrated by Quentin Blake, first published in 1981. It is about a young boy, George, who is forced to stay with his witchlike grandmother, with a penchant for eating bugs.',
    image= 'https://images-na.ssl-images-amazon.com/images/I/91+cH46VDyL.jpg',
    age= '6-9',
    genres= [genre_2, genre_5],
    user= admin
  )
  danny_the_champion_of_the_world = Book(
    title= 'Danny the Champion of the World',
    author= 'Roald Dahl',
    description= 'Danny, the Champion of the World is a 1975 childrens book by Roald Dahl. The plot centres on Danny, a young English boy with a big wagon, and his father, William, who live in a Gypsy caravan fixing cars for a living and partake in poaching pheasants.',
    image= 'https://images-na.ssl-images-amazon.com/images/I/51dlpuRTB1L.jpg',
    age= '6-9',
    genres= [genre_2, genre_5],
    user= admin
  )
  esio_trot = Book(
    title= 'Esio Trot',
    author= 'Roald Dahl',
    description= 'Retired bachelor Mr. Hoppy is hopelessly in love with his neighbor Mrs. Silver, but she is only interested in her pet tortoise Alfie, until Mr. Hoppy hatches an audacious plan to win her love.',
    image= 'https://images-na.ssl-images-amazon.com/images/I/81PoTVk77iL.jpg',
    age= '6-9',
    genres= [genre_2, genre_5],
    user= admin
  )
  the_magic_finger = Book(
    title= 'The Magic Finger',
    author= 'Roald Dahl',
    description= 'The story is about an eight-year-old girl, whose name is never mentioned, who hates hunting, particularly from the neighbouring Gregg family. She tries to talk the Greggs out of it, but either they laugh at her, or they ignore her completely. What they dont know is that the girl has a magic finger.',
    image= 'https://images-na.ssl-images-amazon.com/images/I/91RJ7DOGwhL.jpg',
    age= '6-9',
    genres= [genre_2, genre_5],
    user= admin
  )
  dirty_beasts = Book(
    title= 'Dirty Beasts',
    author= 'Roald Dahl',
    description= 'TThis poem tells the story of a cow called Miss Milky Daisy, who one day grows a pair of gold and silver wings. Because of this, Daisy becomes a bonafide celebrity - expect for a horrid man from Afghanistan. Because of the mans reprehensible behavior, Daisy drops whats called a cowpat on him.',
    image= 'https://images-na.ssl-images-amazon.com/images/I/91Av-Bse-RL.jpg',
    age= '6-9',
    genres= [genre_2, genre_5],
    user= admin
  )    

  charlottes_web = Book(
    title= 'Charlottes Web',
    author= 'E.B. White',
    description= 'Charlottes Web is about a girl named Fern, a pig named Wilbur and a spider called Charlotte. They live on a farm and Fern is horrified when she finds out that Wilbur as a piglet is to be slaughtered. She rescues Wilbur only then to have him sent away from her to her uncles farm where he is friendless and snubbed by the other animals except Charlotte, a spider, and this is where Wilburs adventures begin.',
    image= 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1439632243l/24178._SY475_.jpg',
    age= '6-9',
    user = admin
  )

  harry_potter_stone = Book(
    title= 'Harry Potter and the Philosophers Stone',
    author= 'J. K. Rowling',
    description= 'When mysterious letters start arriving on his doorstep, Harry Potter has never heard of Hogwarts School of Witchcraft and Wizardry. ... Then, on Harrys eleventh birthday, a strange man bursts in with some important news: Harry Potter is a wizard and has been awarded a place to study at Hogwarts.',
    image= 'https://media.bloomsbury.com/rep/bj/9780747532699.jpg',
    age= '12-14',
    genres= [genre_2],
    user = admin
  )
  harry_potter_secrets = Book(
    title= 'Harry Potter and the Chamber of Secrets',
    author= 'J. K. Rowling',
    description= 'A house-elf warns Harry against returning to Hogwarts, but he decides to ignore it. When students and creatures at the school begin to get petrified, Harry finds himself surrounded in mystery.',
    image= 'https://m.media-amazon.com/images/I/51TA3VfN8RL.jpg',
    age= '12-14',
    genres= [genre_2],
    user = admin
  )
  harry_potter_azkaban = Book(
    title= 'Harry Potter and the Prisoner of Azkaban',
    author= 'J. K. Rowling',
    description= 'Harry Potter, along with his best friends, Ron and Hermione, is about to start his third year at Hogwarts School of Witchcraft and Wizardry. Harry cant wait to get back to school after the summer holidays (who wouldnt if they lived with the horrible Dursleys?) But when Harry gets to Hogwarts, the atmosphere is tense. Theres an escaped mass murderer on the loose, and the sinister prison guards of Azkaban have been called in to guard the school . . .',
    image= 'https://images-na.ssl-images-amazon.com/images/I/51vsSNLsBgL.jpg',
    age= '12-14',
    genres= [genre_2],
    user = admin
  )
  harry_potter_fire = Book(
    title= 'Harry Potter and the Goblet of Fire',
    author= 'J. K. Rowling',
    description= 'When the Quidditch World Cup is disrupted by Voldemorts rampaging supporters alongside the resurrection of the terrifying Dark Mark, it is obvious to Harry Potter that, far from weakening, Voldemort is getting stronger. Back at Hogwarts for his fourth year, Harry is astonished to be chosen by the Goblet of Fire to represent the school in the Triwizard Tournament. The competition is dangerous, the tasks terrifying, and true courage is no guarantee of survival – especially when the darkest forces are on the rise.',
    image= 'https://embed.cdn.pais.scholastic.com/v1/channels/sso/products/identifiers/isbn/9780545582957/primary/renditions/700?useMissingImage=true',
    age= '12-14',
    genres= [genre_2],
    user = admin
  )
  harry_potter_phoenix = Book(
    title= 'Harry Potter and the Order of the Phoenix',
    author= 'J. K. Rowling',
    description= 'Harry Potter is furious that he has been abandoned at the Dursleys house for the summer, for he suspects that Voldemort is gathering an army, that he himself could be attacked, and that his so-called friends are keeping him in the dark. Finally rescued by wizard bodyguards, he discovers that Dumbledore is regrouping the Order of the Phoenix – a secret society first formed years ago to fight Voldemort. But the Ministry of Magic is against the Order, lies are being spread by the wizards tabloid, the Daily Prophet, and Harry fears that he may have to take on this epic battle against evil alone.',
    image= 'https://media.bloomsbury.com/rep/f/9781408894750.jpg',
    age= '12-14',
    genres= [genre_2],
    user = admin
  )
  harry_potter_prince = Book(
    title= 'Harry Potter and the Half-Blood Prince ',
    author= 'J. K. Rowling',
    description= 'Suspicion and fear blow through the wizarding world as news of the Dark Lords attack on the Ministry of Magic spreads. Harry has not told anyone about the future predicted by the prophecy in the Department of Mysteries, nor how deeply what happened to Sirius Black affected him. Hes desperate for Professor Dumbledore to arrive and take him away from the Dursleys – but Hogwarts may not be the safe haven from Voldemorts Dark Forces that it once was. In his sixth year, the names Black, Malfoy, Lestrange and Snape will haunt Harry with shades of trust and treachery as he discovers the secret behind the mysterious Half-Blood Prince – and Dumbledore prepares him to face his own terrifying destiny.',
    image= 'https://images-na.ssl-images-amazon.com/images/I/91YH0ZtB9XL.jpg',
    age= '12-14',
    genres= [genre_2],
    user = admin
  )
  harry_potter_hallows = Book(
    title= 'Harry Potter and the Deathly Hallows ',
    author= 'J. K. Rowling',
    description= 'Harry Potter is preparing to leave the Dursleys and Privet Drive for the last time. But the future that awaits him is full of danger, not only for him, but for anyone close to him – and Harry has already lost so much. Only by destroying Voldemorts remaining Horcruxes can Harry free himself and overcome the Dark Lords forces of evil. In this dramatic conclusion to the Harry Potter series, Harry must leave his most loyal friends behind, and in a final perilous journey find the strength and the will to face his terrifying destiny: a deadly confrontation that is his alone to fight.',
    image= 'https://kbimages1-a.akamaihd.net/35cd6228-f6b1-4b30-8edf-b56bf1738180/353/569/90/False/harry-potter-and-the-deathly-hallows-4.jpg',
    age= '12-14',
    genres= [genre_2],
    user = admin
  )

  the_tiger_came_to_tea = Book(
    title= 'The Tiger Who Came To Tea',
    author= 'Judith Kerr',
    description= 'His favourite was Rooibos!',
    image= 'tbc3',
    age= '6-9',
    genres= [genre_2, genre_7],
    user = admin   
  )


  the_gruffalo = Book(
    title= 'The Gruffalo',
    author= 'Julia Donaldson',
    description= 'A rhyming story about a mouse and a monster',
    image= 'tbc4',
    age= '6-9',
    genres= [genre_2, genre_5, genre_7],
    user = admin    
  )

  the_hungry_caterpillar = Book(
    title= 'The Very Hungry Caterpillar',
    author= 'Eric Carle',
    description= 'Soooooo hungry!',
    image= 'tbc5',
    age= '6-9',
    genres= [genre_2, genre_5, genre_7],
    user = admin   
  )

  twits = Book(
    title= 'The Twits',
    author= 'Roald Dahl',
    description= 'They really are twits',
    image= 'tbc6',
    age= '6-9',
    genres= [genre_2],
    user = admin    
  )

  codename_bananas = Book(
    title= 'Codename Bananas',
    author= 'David Walliams',
    description= 'Double-O bananas',
    image= 'tbc7',
    age= '6-9',
    genres= [genre_2],
    user = admin    
  )

  stick_man = Book(
    title= 'Stick Man',
    author= 'Julia Donaldson',
    description= 'Surprisingly scary!',
    image= 'tbc8',
    age= '6-9',
    genres= [genre_2, genre_5],
    user = admin    
  )


  print('Books created')

  comment1 = Comment(
    content = 'This book is fun to read, My little ones love it',
    book=the_hungry_caterpillar,
    user = admin
  )

  print('Comment created') 
  print('Adding to database')


  db.session.add(the_hungry_caterpillar)
  # db.session.add(charlie_and_the_chocolate_factory)
  # db.session.add(charlottes_web)
  # db.session.add(harry_potter_stone)
  db.session.add(the_tiger_came_to_tea)
  db.session.add(the_gruffalo)
  db.session.add(tracy_beaker)
  db.session.add(hetty_feather)
  db.session.add(tracy_beaker2)
  db.session.add(double_act)
  db.session.add(best_friends)
  db.session.add(green_eggs_and_ham)
  db.session.add(how_the_grinch_stole_christmas)
  db.session.add(one_fish_two_fish)
  db.session.add(oh_the_places_you_will_go)
  db.session.add(fox_in_socks)
  db.session.add(the_lorex)
  db.session.add(horton_hears_a_who)
  db.session.add(hop_on_pop)
  db.session.add(abc)
  db.session.add(matilda)
  db.session.add(giant_peach)
  db.session.add(the_bfg)
  db.session.add(the_witches)
  db.session.add(fantastic_mr_fox)
  db.session.add(georges_marvellous_medicine)
  db.session.add(danny_the_champion_of_the_world)
  db.session.add(the_magic_finger)
  db.session.add(dirty_beasts)
  db.session.add(harry_potter_secrets)
  db.session.add(harry_potter_azkaban)
  db.session.add(harry_potter_fire)
  db.session.add(harry_potter_phoenix)
  db.session.add(harry_potter_prince)
  db.session.add(harry_potter_prince)
  db.session.add(the_hungry_caterpillar)
  db.session.add(twits)
  db.session.add(codename_bananas)
  db.session.add(stick_man)
  db.session.add(comment1)
  db.session.add(genre_1)
  db.session.add(genre_2)
  db.session.add(genre_3)
  db.session.add(genre_4)
  db.session.add(genre_5)
  db.session.add(genre_6)
  db.session.add(genre_7)
  db.session.commit()


  print('Completed')



