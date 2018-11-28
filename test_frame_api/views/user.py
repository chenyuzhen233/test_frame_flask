from test_frame_api import db, app
from models import User
from response import result_code
from flask import jsonify, abort, make_response, request


@app.route('/')
def hello():
    response = {
        "code":0000,
        "data":"hello,friend!",
        "msg":result_code[0000]
    }
    return jsonify(response)

@app.route('/user/selectUserById/<int:id>')
def selectUserById(id):
    user = User.query.filter_by(id=id).one()
    if user:
        response = {
            "code": 1001,
            "data": None,
            "msg": result_code[1001]
        }
    else:
        response = {
            "code": 0000,
            "data": user.__str__(),
            "msg": result_code[0000]
        }
    return jsonify(response)

@app.route('/api/selectAll')
def selectAll():
    result['code'] = '10000'
    result['msg'] = UserInterface.selectAll()
    return json.dumps(result)

@app.route('/api/insertUser', methods=['POST'])
def insertUser():
    user = User()
    dict_data = request.form.to_dict()
    user.name = dict_data['name']
    result['msg'] = UserInterface.insertUser(user)
    result['code'] = '10000'
    return json.dumps(result)

@app.route('/api/deleteUserById', methods=['POST'])
def deleteUserById(self, user):
    user = User()
    dict_data = request.form.to_dict()
    user.id = dict_data['id']
    result['msg'] = UserInterface.deleteUserById(user)
    result['code'] = '10000'
    return json.dumps(result)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404