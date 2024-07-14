from flask_sqlalchemy import SQLAlchemy
from . import db
from . import Familiar
from services.familiar import add_new_familiar
class NPC(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    npcID = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), unique=False, nullable=False)
    maxFamiliarLevel = db.Column(db.Integer, unique=False, nullable=False) #start from 1
    firstFamiliarLevelID = db.Column(db.Integer, unique=True, nullable=False)
    def __init__(self, npcID, name, maxFamiliarLevel, firstFamiliarLevelID = None):
        """
        create a NPC
        :param npcID: string;
        :param name: string;
        :param maxFamiliarLevel: integer;
        :param firstFamiliarLevelID: integer;
        """
        self.npcID = npcID
        self.name = name
        self.maxFamiliarLevel = maxFamiliarLevel
        self.firstFamiliarLevelID = firstFamiliarLevelID
    def __repr__(self):
        return f'<NPC {self.npcID, self.name}>'