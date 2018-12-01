from test_frame_api import db, app
from models import Project, Token
from response import result_code
from flask import jsonify, request

import datetime


@app.route('/project/selectProjectById', methods=['POST'])
def selectProjectById():
    project = Project.query.filter_by(id=request.form.get('id', 0)).first()
    if project:
        response = {
            "code": 00000,
            "data": project.__str__(),
            "msg": result_code[00000]
        }
    else:
        response = {
            "code": 30001,
            "data": None,
            "msg": result_code[30001]
        }
    return jsonify(response)

@app.route('/project/selectAllProject', methods=['POST'])
def selectAllProject():
    token = Token.query.filter_by(token=request.form.get('token',None)).first()
    if token:
        if token.expire_time > datetime.datetime.now():
            projects = [p.__str__() for p in Project.query.all()]
            response = {
                "code":00000,
                "data":projects,
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

@app.route('/project/insertProject', methods=['POST'])
def insertProject():
    project = Project(name=request.form.get('name', None),
                      remarks=request.form.get('remarks', None))
    try:
        if not project.name:
            raise BaseException
        db.session.add(project)
        db.session.commit()
        response = {
            "code": 00000,
            "data": project.__str__(),
            "msg": result_code[00000]
        }
    except:
        response = {
            "code": 30002,
            "data": None,
            "msg": result_code[30002]
        }
    return jsonify(response)

@app.route('/project/deleteProjectById', methods=['POST'])
def deleteProjectById():
    project = Project.query.filter_by(id=request.form.get('id', None)).first()
    try:
        db.session.delete(project)
        db.session.commit()
        response = {
            "code": 00000,
            "data": None,
            "msg": result_code[00000]
        }
    except:
        response = {
            "code": 30003,
            "data": None,
            "msg": result_code[30003]
        }
    return jsonify(response)