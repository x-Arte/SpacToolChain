from flask_sqlalchemy import SQLAlchemy
from . import db

class Selection(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(255), unique=False, nullable=True)
    nextDialogueID = db.Column(db.Integer, unique=False, nullable=True)
    nextSelection = db.Column(db.Integer, unique=False, nullable=True)
    conditionID = db.Column(db.Integer, unique=False, nullable=True)
    triggerID = db.Column(db.Integer, unique=False, nullable=True)