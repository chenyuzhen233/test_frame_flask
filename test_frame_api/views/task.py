from test_frame_api import db, app
from ..models import Task, Interface, Case
from ..response import result_code
from flask import jsonify, request

import datetime


@app.route('/task/selectTaskById', methods=['POST'])
def selectTaskById():
    task = Task.query.filter_by(id=request.form.get('id', 0)).first()
    if task:
        response = {
            "code": 00000,
            "data": task.__str__(),
            "msg": result_code[00000]
        }
    else:
        response = {
            "code": 70001,
            "data": None,
            "msg": result_code[70001]
        }
    return jsonify(response)


@app.route('/task/selectAllTask', methods=['POST', 'GET'])
def selectAllTask():
    task = [t.__str__() for t in Task.query.all()]
    response = {
        "code": 00000,
        "data": task,
        "msg": result_code[00000]
    }
    return jsonify(response)


@app.route('/task/insertTask', methods=['POST'])
def insertTask():
    task = Task(name=request.form.get('name', None),
                user_id=request.form.get('user_id', None),
                status=request.form.get('status', None),
                case_id=request.form.get('case_id', None),
                interface_id=request.form.get('interface_id', None),
                project_id=request.form.get('project_id', None),
                host=request.form.get('host', None),
                remarks=request.form.get('remarks', None),
                start_time=request.form.get('start_time', None),
                create_time=datetime.datetime.today())
    try:
        if not task.name:
            raise BaseException
        db.session.add(task)
        db.session.commit()
        response = {
            "code": 00000,
            "data": task.__str__(),
            "msg": result_code[00000]
            }
    except:
        response = {
            "code": 70002,
            "data": None,
            "msg": result_code[70002]
            }
    return jsonify(response)


@app.route('/task/deleteTaskById', methods=['POST'])
def deleteTaskById():
    task = Task.query.filter_by(id=request.form.get('id', None)).first()
    try:
        db.session.delete(task)
        db.session.commit()
        response = {
            "code": 00000,
            "data": None,
            "msg": result_code[00000]
        }
    except:
        response = {
            "code": 70003,
            "data": None,
            "msg": result_code[70003]
        }
    return jsonify(response)
