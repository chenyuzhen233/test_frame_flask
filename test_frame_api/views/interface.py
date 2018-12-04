from test_frame_api import db, app
from ..models import Interface, Token
from ..response import result_code
from flask import jsonify, request

import datetime


@app.route('/interface/selectInterfaceById', methods=['POST'])
def selectInterfaceById():
    interface = Interface.query.filter_by(id=request.form.get('id', 0)).first()
    if interface:
        response = {
            "code": 00000,
            "data": interface.__str__(),
            "msg": result_code[00000]
        }
    else:
        response = {
            "code": 50001,
            "data": None,
            "msg": result_code[50001]
        }
    return jsonify(response)

@app.route('/interface/selectAllInterface', methods=['POST'])
def selectAllInterface():
    token = Token.query.filter_by(token=request.form.get('token',None)).first()
    if token:
        if token.expire_time > datetime.datetime.now():
            interface = [i.__str__() for i in Interface.query.all()]
            response = {
                "code":00000,
                "data":interface,
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

@app.route('/interface/insertInterface', methods=['POST'])
def insertInterface():
    interface = Interface(name=request.form.get('name', None),
                          module_id=request.form.get('module_id', None),
                          remarks=request.form.get('remarks', None),
                          create_time=datetime.datetime.today())
    try:
        if not interface.name:
            raise BaseException
        db.session.add(interface)
        db.session.commit()
        response = {
            "code": 00000,
            "data": interface.__str__(),
            "msg": result_code[00000]
            }
    except:
        response = {
            "code": 50002,
            "data": None,
            "msg": result_code[50002]
            }
    return jsonify(response)

@app.route('/interface/deleteInterfaceById', methods=['POST'])
def deleteInterfaceById():
    interface = Interface.query.filter_by(id=request.form.get('id', None)).first()
    try:
        db.session.delete(interface)
        db.session.commit()
        response = {
            "code": 00000,
            "data": None,
            "msg": result_code[00000]
        }
    except:
        response = {
            "code": 50003,
            "data": None,
            "msg": result_code[50003]
        }
    return jsonify(response)