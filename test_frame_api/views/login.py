from test_frame_api import db, app
from models import  User, Token
from response import result_code
from flask import jsonify, request

import random
import string
import datetime

@app.route('/login/login', methods=['POST'])
def login():
    user =  User.query.filter_by(name=request.form.get('name', None)).first()
    if user and user.password == request.form.get('password', None):
        token = Token(token=''.join(random.sample(string.ascii_letters + string.digits, 20)),
                      user_id=user.id,
                      create_time=datetime.datetime.today(),
                      expire_time=datetime.datetime.today() + datetime.timedelta(days=7))
        print(datetime.date.today())
        db.session.add(token)
        db.session.commit()
        response = {
            "code": 00000,
            "data": token.__str__(),
            "msg": result_code[00000]
        }
    else:
        response = {
            "code": 98001,
            "data": None,
            "msg": result_code[98001]
        }
    return jsonify(response)

@app.route("/login/logout", methods=['POST'])
def logout():
    user = User.query.filter_by(name=request.form.get('name', None)).first()
    if user:
        tokens = Token.query.filter_by(user_id=user.id).all()
        [db.session.delete(t) for t in tokens]
        db.session.commit()
        response = {
            "code": 00000,
            "data": None,
            "msg": result_code[00000]
        }
    else:
        response = {
            "code": 98002,
            "data": None,
            "msg": result_code[98002]
        }
    return jsonify(response)