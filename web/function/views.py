from . import function
from flask import request, jsonify
from models import db
from models.Condition import Condition
from models.Trigger import Trigger
import services.function
@function.route("/function/add", methods=['POST'])
def add_function_by_json():
    add_function_data = request.get_json()
    try:
        if add_function_data['isCondition']:
            new_condition = Condition(name=add_function_data["functionName"], description=add_function_data["description"])
            db.session.add(new_condition)
        else:
            new_trigger = Trigger(name=add_function_data["functionName"], description=add_function_data["description"])
            db.session.add(new_trigger)
        db.session.commit()
        status_code = 200
        result = {}
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred: {e}")
        status_code = 400
        result = {}

    return jsonify(result), status_code

@function.route('/function/delete', methods=['POST'])
def delete_function_by_json():
    delete_function_data = request.get_json()
    if delete_function_data['isCondition']:
        func = Condition.query.get(int(delete_function_data['id']))
    else:
        func = Trigger.query.get(int(delete_function_data['id']))
    if func:
        db.session.delete(func)
        db.session.commit()
        status_code = 200
        result = {}
    else:
        db.session.rollback()
        status_code = 400
        result = {}
    return jsonify(result), status_code

@function.route('/function/update', methods=['POST'])
def update_function_by_json():
    update_function_data = request.get_json()
    if update_function_data['isCondition']:
        func = Condition.query.get(int(update_function_data['id']))
    else:
        func = Trigger.query.get(int(update_function_data['id']))
    if func:
        func.name = update_function_data['functionName']
        func.description = update_function_data['description']
        db.session.commit()
        status_code = 200
        result = {}
    else:
        db.session.rollback()
        status_code = 400
        result = {}
    return jsonify(result), status_code

@function.route('/function/getList', methods=['POST'])
def get_function_list_by_json():
    func_type = request.get_json()
    try:
        if func_type["isCondition"]:
            all_func = Condition.query.all()
        else:
            all_func = Trigger.query.all()
        func_list = [services.function.to_dict(func) for func in all_func]
        status_code = 200
        result = {"list": func_list}
    except:
        db.session.rollback()
        status_code = 400
        result = {}
    return jsonify(result), status_code




