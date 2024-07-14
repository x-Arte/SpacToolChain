from flask_sqlalchemy import SQLAlchemy
from . import db

class Familiar(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # db store
    nextFamiliarLevelID = db.Column(db.Integer, unique=False, nullable=True)
    firstDialogueID = db.Column(db.Integer, unique=False, nullable=True)
    # static attribute
    maxSubFamiliarLevel = db.Column(db.Integer, unique=False, nullable=False)
    defaultNextDialogue = db.Column(db.Integer, unique=False, nullable=True)

    def __init__(self, maxSubFamiliarLevel, nextFamiliarLevelID = None, firstDialogueID = None, defaultNextDialogue = None):
        """
        create a Familiar Level
        :param maxSubFamiliarLevel: integer;
        :param nextFamiliarLevelID: integer; link node
        :param firstDialogueID: integer; can be None when creating
        :param defaultNextDialogue: integer; attribute in game, not in db
        """
        self.maxSubFamiliarLevel = maxSubFamiliarLevel
        self.nextFamiliarLevelID = nextFamiliarLevelID
        self.firstDialogueID = firstDialogueID
        self.defaultNextDialogue = defaultNextDialogue

    def __repr__(self):
        return f'<FamiliarLevel: {self.id, self.maxSubFamiliarLevel}>'