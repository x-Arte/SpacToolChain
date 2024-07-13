from . import npc
from flask import request, jsonify
from models import db
from models.NPC import NPC
import sevices.npc

@npc.route('/npc/add', methods=['POST'])
def add_npc_by_json():
    add_npc_data = request.get_json()
    try:
        new_npc = sevices.npc.create_new_npc(npcID=add_npc_data['npcID'], name=add_npc_data['name'], familiarList=add_npc_data['familiarList'])
        db.session.add(new_npc)
        db.session.commit()
        status_code = 200
        result = {
            "id": new_npc.id
        }
    except:
        db.session.rollback()
        status_code = 400
        result = {
            "msg": "Failed to add a new NPC. Please check the query data.",
        }
    return jsonify(result), status_code

@npc.route('/npc/delete', methods=['POST'])
def delete_npc_by_json():
    delete_npc_id = request.get_json()['id']
    npc = NPC.query.get(int(delete_npc_id))
    if npc:
        delete = sevices.npc.delete_npc(npc)
        if delete:
            status_code = 200
            result = {}
        else:
            status_code = 500
            result = {
                "msg": "Failed to delete the npc and its related data. Please check the database or contact the admin."
            }
    else:
        db.session.rollback()
        status_code = 400
        result = {
            "msg": "Failed to find the npc. Please check the query data."
        }
    return jsonify(result), status_code