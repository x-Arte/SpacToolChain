from flask_sqlalchemy import SQLAlchemy
from . import db

class NPC(db.Model):
    id = db.Column(db.String(8), primary_key=True)
    npcID = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), unique=False, nullable=False)
    maxFamiliarLevel = db.Column(db.Integer(255), unique=False, nullable=False)
    firstFamiliarLevelID = db.Column(db.String(20), unique=True, nullable=False)
    def __repr__(self):
        return f'<NPC {self.npcID, self.name}>'