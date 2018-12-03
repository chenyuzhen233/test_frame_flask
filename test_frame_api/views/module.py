from test_frame_api import db, app
from models import Module, Token
from response import result_code
from flask import jsonify, request

import datetime


@app.route('/module/selectModuleById', methods=['POST'])
def selectModuleById():
    project = Module.query.filter_by(id=request.form.get('id', 0)).first()
    if project:
        response = {
            "code": 00000,
            "data": project.__str__(),
            "msg": result_code[00000]
        }
    else:
        response = {
            "code": 40001,
            "data": None,
            "msg": result_code[40001]
        }
    return jsonify(response)

@app.route('/module/selectAllModule', methods=['POST'])
def selectAllModule():
    token = Token.query.filter_by(token=request.form.get('token',None)).first()
    if token:
        if token.expire_time > datetime.datetime.now():
            module = [m.__str__() for m in Module.query.all()]
            response = {
                "code":00000,
                "data":module,
                "msg":result_code[00000]
            }
        else:
            response = {
                "code": 20001,
                "data": None,
                "msg": result_code[20001]
            }
    else:
        response = {
            "code": 20002,
            "data": None,
            "msg": result_code[20002]
        }
    return jsonify(response)

@app.route('/module/insertModule', methods=['POST'])
def insertModule():
    module = Module(name=request.form.get('name', None),
                    project_id=request.form.get('project_id', None),
                    remarks=request.form.get('remarks', None),
                    create_time=datetime.datetime.today())
    try:
        if not module.name:
            raise BaseException
        db.session.add(module)
        db.session.commit()
        response = {
            "code": 00000,
            "data": module.__str__(),
            "msg": result_code[00000]
            }
    except:
        response = {
            "code": 40002,
            "data": None,
            "msg": result_code[40002]
            }
    return jsonify(response)

@app.route('/module/deleteModuleById', methods=['POST'])
def deleteModuleById():
    module = Module.query.filter_by(id=request.form.get('id', None)).first()
    try:
        db.session.delete(module)
        db.session.commit()
        response = {
            "code": 00000,
            "data": None,
            "msg": result_code[00000]
        }
    except:
        response = {
            "code": 40003,
            "data": None,
            "msg": result_code[40003]
        }
    return jsonify(response)