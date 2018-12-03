from test_frame_api import db, app
from models import User, Token
from response import result_code
from flask import jsonify, abort, request

import datetime


@app.route('/')
def hello():
    response = {
        "code":00000,
        "data":"hello,friend!",
        "msg":result_code[00000]
    }
    return jsonify(response)

@app.route('/user/selectUserById', methods=['POST'])
def selectUserById():
    user = User.query.filter_by(id=request.form.get('id', 0)).first()
    if user:
        response = {
            "code": 00000,
            "data": user.__str__(),
            "msg": result_code[00000]
        }
    else:
        response = {
            "code": 10001,
            "data": None,
            "msg": result_code[10001]
        }
    return jsonify(response)

@app.route('/user/selectAllUser', methods=['POST'])
def selectAllUser():
    token = Token.query.filter_by(token=request.form.get('token', None)).first()
    if token:
        if token.expire_time > datetime.datetime.now():
            users = [u.__str__() for u in User.query.all()]
            response = {
                "code":00000,
                "data":users,
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

@app.route('/user/insertUser', methods=['POST'])
def insertUser():
    user = User(name=request.form.get('name', None),
                password=request.form.get('password', None))
    try:
        if not user.name:
            raise BaseException
        db.session.add(user)
        db.session.commit()
        response = {
            "code": 00000,
            "data": user.__str__(),
            "msg": result_code[00000]
        }
    except:
        response = {
            "code": 10002,
            "data": None,
            "msg": result_code[10002]
        }
    return jsonify(response)

@app.route('/user/deleteUserById', methods=['POST'])
def deleteUserById():
    user = User.query.filter_by(id=request.form.get('id', None)).first()
    try:
        if not user.id:
            raise BaseException
        db.session.delete(user)
        db.session.commit()
        response = {
            "code": 00000,
            "data": None,
            "msg": result_code[00000]
        }
    except:
        response = {
            "code": 10003,
            "data": None,
            "msg": result_code[10003]
        }
    return jsonify(response)

@app.errorhandler(404)
def not_found(error):
    response = {
        "code": 99001,
        "data": None,
        "msg": result_code[99001]
    }
    return jsonify(response), 404