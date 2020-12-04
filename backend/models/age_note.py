from app import db

ages_notes_join = db.Table('ages_notes',
  db.Column('note_id', db.Integer, db.ForeignKey('notes.id'), primary_key=True),
  db.Column('age_id', db.Integer, db.ForeignKey('ages.id'), primary_key=True)