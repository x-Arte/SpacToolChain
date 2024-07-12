from flask_sqlalchemy import SQLAlchemy
from . import db

class Familiar(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)