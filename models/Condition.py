from flask_sqlalchemy import SQLAlchemy
from . import db
class Condition(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)

    def __repr__(self):
        return f'<Condition {self.name, self.description}>'

    def to_dict(self):
        return {
            "id": str(self.id),
            "functionName": self.name,
            "description": self.description
        }
