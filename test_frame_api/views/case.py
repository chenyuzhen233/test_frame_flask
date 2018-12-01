from test_frame_api import db, app
from models import Case, Token
from response import result_code
from flask import jsonify, request

import datetime


@app.route('/case/selectCaseById', methods=['POST'])
def selectCaseById():
    case = Case.query.filter_by(id=request.form.get('id', 0)).first()
    if case:
        response = {
            "code": 00000,
            "data": case.__str__(),
            "msg": result_code[00000]
        }
    else:
        response = {
            "code": 60001,
            "data": None,
            "msg": result_code[60001]
        }
    return jsonify(response)


@app.route('/case/selectAllCase', methods=['POST'])
def selectAllCase():
    token = Token.query.filter_by(token=request.form.get('token', None)).first()
    if token:
        if token.expire_time > datetime.datetime.now():
            case = [i.__str__() for i in Case.query.all()]
            response = {
                "code": 00000,
                "data": case,
                "msg": result_code[00000]
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


@app.route('/case/insertCase', methods=['POST'])
def insertCase():
    case = Case(name=request.form.get('name', None),
                interface_id=request.form.get('interface_id', None),
                method=request.form.get('method', None),
                params=request.form.get('params', None),
                url=request.form.get('url', None),
                relation=request.form.get('relation', None),
                relation_params=request.form.get('relation_params', None),
                save_params=request.form.get('save_params', None),
                remarks=request.form.get('remarks', None))
    try:
        if not case.name:
            raise BaseException
        db.session.add(case)
        db.session.commit()
        response = {
            "code": 00000,
            "data": case.__str__(),
            "msg": result_code[00000]
            }
    except:
        response = {
            "code": 60002,
            "data": None,
            "msg": result_code[60002]
            }
    return jsonify(response)


@app.route('/case/deleteCaseById', methods=['POST'])
def deleteCaseById():
    case = Case.query.filter_by(id=request.form.get('id', None)).first()
    try:
        db.session.delete(case)
        db.session.commit()
        response = {
            "code": 00000,
            "data": None,
            "msg": result_code[00000]
        }
    except:
        response = {
            "code": 60003,
            "data": None,
            "msg": result_code[60003]
        }
    return jsonify(response)