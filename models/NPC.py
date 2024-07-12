from flask_sqlalchemy import SQLAlchemy
from . import db
from . import Familiar
class NPC(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    npcID = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), unique=False, nullable=False)
    maxFamiliarLevel = db.Column(db.Integer, unique=False, nullable=False) #start from 1
    firstFamiliarLevelID = db.Column(db.Integer, unique=True, nullable=False)
    def __init__(self, npcID, name, familiarList):
        """
        :param npcID: npcID
        :param name: name of NPC
        :param familiarList: maxSubFamiliarLevel List
        """
        self.npcID = npcID
        self.name = name
        self.maxFamiliarLevel = len(familiarList) + 1
        for i in range(self.maxFamiliarLevel):
            # TODO: create muti Familiars
            self.firstFamiliarLevelID = 1
    def __repr__(self):
        return f'<NPC {self.npcID, self.name}>'