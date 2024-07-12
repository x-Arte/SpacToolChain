from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# def init_app(app):
#     db.init_app(app)

from . import NPC
from . import Familiar
from . import Condition
from . import Trigger