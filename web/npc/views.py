from . import npc
from flask import request, jsonify
from models import db
from models.NPC import NPC

@npc.route('/npc/add', methods=['POST'])
def add_npc_by_json():
    add_npc_data = request.get_json()
    try:
        id =
        new_npc = NPC(npcId=add_npc_data[''])
        db.session.add(new_npc)
        db.session.commit()
        status_code = 200
        result = {
            "id": id,
        }
    except:
        db.session.rollback()
        status_code = 400
        result = {
            "msg": "Failed to add a new NPC. Please check the query data.",
            "code": status_code
        }
        return jsonify(result), status_code

@npc.route('/npc/delete', methods=['POST'])
def delete_npc_by_json():
    delete_npo_data = request.get_json()
    npc = NPC.query.get()