from flask_sqlalchemy import SQLAlchemy
from . import db


class Trigger(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)

    def __repr__(self):
        return f'<Trigger {self.name, self.description}>'

