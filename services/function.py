from models.Condition import Condition
from models.Trigger import Trigger
from models import db

def to_dict(function):
    return {
        "id": str(function.id),
        "functionName": function.name,
        "description": function.description
    }