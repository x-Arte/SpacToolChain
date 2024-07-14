from . import npc
from flask import request, jsonify
from models import db
from models.NPC import NPC
import services.npc

@npc.route('/npc/add', methods=['POST'])
def add_npc_by_json():
    add_npc_data = request.get_json()
    try:
        new_npc = services.npc.create_new_npc(npcID=add_npc_data['npcID'], name=add_npc_data['name'], familiarList=add_npc_data['familiarList'])
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
        delete = services.npc.delete_npc(npc)
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
@npc.route('/npc/update', methods=['POST'])
def update_npc_by_json():
    update_npc_data = request.get_json()
    npc = NPC.query.get(int(update_npc_data['id']))
    if npc:
        update = services.npc.update_npc(npc, npcID=update_npc_data['npcID'], name=update_npc_data['name'], familiarList=update_npc_data['familiarList'])
        if update:
            status_code = 200
            result = {}
        else:
            status_code = 500
            result = {
                "msg": "Failed to update the npc and its related data. Please check the query data."
            }
    else:
        db.session.rollback()
        status_code = 400
        result = {
            "msg": "Failed to find the npc. Please check the query data."
        }
    return jsonify(result), status_code

@npc.route('/npc/getInfo', methods=['POST'])
def get_npc_info_by_json():
    get_npc_data = request.get_json()
    npc = NPC.query.get(int(get_npc_data['id']))
    if npc:
        try:
            status_code = 200
            result = services.npc.to_dict(npc, details=True)
        except:
            status_code = 500
            result = {"msg": "Failed to get the npc and its related data. Please check the query data."}
    else:
        db.session.rollback()
        status_code = 400
        result = {
            "msg": "Failed to find the npc. Please check the query data."
        }
    return jsonify(result), status_code
@npc.route('/npc/getList', methods=['POST'])
def get_npc_list_by_json():
    try:
        all_npc = NPC.query.all()
        npc_list = [services.npc.to_dict(npc, details=False) for npc in all_npc]
        status_code = 200
        result = {"npcList": npc_list}
    except:
        db.session.rollback()
        status_code = 400
        result = {}
    return jsonify(result), status_code