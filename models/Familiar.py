from flask_sqlalchemy import SQLAlchemy
from . import db

class Familiar(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    maxFamiliarLevel = db.Column(db.Integer, unique=False, nullable=False)
    nextFamiliarLevel = db.Column(db.Integer, unique=True, nullable=True)
    firstDialogue = db.Column(db.Integer, unique=False, nullable=True)