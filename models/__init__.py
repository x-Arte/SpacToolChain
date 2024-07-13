from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# def init_app(app):
#     db.init_app(app)

# notify: before init, all the data structure (table) import here should be completed
from . import NPC
from . import Familiar
from . import Condition
from . import Trigger
from . import Dialogue
from . import Selection