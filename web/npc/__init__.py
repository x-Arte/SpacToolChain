from flask import Blueprint
npc = Blueprint('npc', __name__)
from . import views