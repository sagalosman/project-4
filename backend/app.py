from flask import Flask
from environment.config import db_URI 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from controllers import users
from flask_bcrypt import Bcrypt
# from models.user import User


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = db_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


ma = Marshmallow(app)
bcrypt = Bcrypt(app)

# app.register_blueprint(books.router, url_prefix="/api")
app.register_blueprint(users.router, url_prefix="/api")


from controllers import books
app.register_blueprint(books.router, url_prefix="/api")

