from flask_sqlalchemy import SQLAlchemy
from . import db

class Dialogue(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #not sure
    nextDialogueID = db.Column(db.Integer, unique=False, nullable=True)
    firstSelectionID = db.Column(db.Integer, unique=False, nullable=True)

    defaultNextDialogue = db.Column(db.Integer, unique=False, nullable=True)
    content = db.Column(db.Text, unique=False, nullable=True)
    speaker = db.Column(db.String(255), unique=False, nullable=True)
    jumpMethod = db.Column(db.Integer, unique=False, nullable=True)
    posx = db.Column(db.Float, unique=False, nullable=True)
    posy = db.Column(db.Float, unique=False, nullable=True)