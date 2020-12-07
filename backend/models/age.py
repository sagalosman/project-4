# from app import db
# from models.base import BaseModel
# from models.user import User


# class Age(db.Model, BaseModel):

#   __tablename__ = 'ages'

#   age = db.Column(db.String(10), unique=False, nullable=True)

  
#    # ! This code in 1-M Relationships points to the ONE side
#   # CREATE the actual column in the database
#   user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#    # Associate the 2 models together
#   user = db.relationship('User', backref='ages')



