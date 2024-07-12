from flask import Flask
from models import db
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['JSON_AS_ASCII'] = False
    app.config['SQLALCHEMY_ECHO'] = False

    #initialize the database
    db.init_app(app)

    # register blueprint separately
    from .npc import npc
    from .function import function
    app.register_blueprint(npc)# dont use url_preflix
    app.register_blueprint(function)

    # create database table
    with app.app_context():
        db.create_all()
    return app