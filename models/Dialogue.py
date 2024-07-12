from flask_sqlalchemy import SQLAlchemy
from . import db

class Dialogue(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #TODO: not sure
    jumpMethod = db.Column(db.Integer, unique=False, nullable=True)
    firstSelectionID = db.Column(db.Integer, unique=False, nullable=True)
    defaultNextDialogue = db.Column(db.Integer, unique=False, nullable=True)
    nextDialogueID = db.Column(db.Integer, unique=False, nullable=True)
    content = db.Column(db.Text, unique=False, nullable=True)
    speaker = db.Column(db.String(255), unique=False, nullable=True)

