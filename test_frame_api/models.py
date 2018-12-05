from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    # table name
    __tablename__ = "user"
    # table structure
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, password, create_time):
        self.name = name
        self.password = password
        self.create_time = create_time

    def __str__(self):
        response = {
            "id": self.id,
            "name": self.name,
            "password": self.password,
            "create_time": self.create_time
        }
        return response


class Token(db.Model):
    # table name
    __tablename__ = "token"
    # table structure
    id = db.Column(db.Integer, primary_key = True)
    token = db.Column(db.String(255), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", backref="token_of_user")

    create_time = db.Column(db.DateTime, nullable=False)
    expire_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, token, user_id, create_time, expire_time):
        self.token = token
        self.user_id = user_id
        self.create_time = create_time
        self.expire_time = expire_time

    def __str__(self):
        response = {
            "id": self.id,
            "user_id": self.user_id,
            "token": self.token,
            "create_time": self.create_time,
            "expire_time": self.expire_time
        }
        return response


class Project(db.Model):
    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    remarks = db.Column(db.String(255), nullable=True)
    create_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, create_time, remarks=None):
        self.name = name
        self.remarks = remarks
        self.create_time = create_time

    def __str__(self):
        response = {
            "id": self.id,
            "name": self.name,
            "remarks": self.remarks,
            "create_time": self.create_time
        }
        return response


class Module(db.Model):
    __tablename__ = "module"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    project = db.relationship("Project", backref="module_of_project")

    remarks = db.Column(db.String(255), nullable=True)
    create_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, project_id, create_time, remarks=None):
        self.name = name
        self.project_id = project_id
        self.remarks = remarks
        self.create_time = create_time

    def __str__(self):
        response = {
            "id": self.id,
            "name": self.name,
            "project": self.project.__str__(),
            "remarks": self.remarks,
            "create_time": self.create_time
        }
        return response


class Interface(db.Model):
    __tablename__ = "interface"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'))
    module = db.relationship("Module", backref="interface_of_module")
    remarks = db.Column(db.String(255), nullable=True)
    create_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, module_id, create_time, remarks=None):
        self.name = name
        self.module_id = module_id
        self.remarks = remarks
        self.create_time = create_time

    def __str__(self):
        response = {
            "id": self.id,
            "name": self.name,
            "module": self.module.__str__(),
            "remarks": self.remarks,
            "create_time": self.create_time
        }
        return response


class Case(db.Model):
    __tablename__ = "case"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    interface_id = db.Column(db.Integer, db.ForeignKey('interface.id'))
    interface = db.relationship("Interface", backref="case_of_interface")

    status = db.Column(db.Integer, nullable=False)
    method = db.Column(db.Integer, nullable=False)
    params = db.Column(db.String(2000), nullable=True)
    url = db.Column(db.String(255), nullable=False)
    relation = db.Column(db.Integer, nullable=False)
    relation_params = db.Column(db.String(2000), nullable=True)
    save_params = db.Column(db.String(2000), nullable=True)

    remarks = db.Column(db.String(255), nullable=True)
    create_time = db.Column(db.DateTime, nullable=True)

    def __init__(self, name, interface_id, method, params, url, relation,
                 relation_params, save_params, create_time, status, remarks=None):
        self.name = name
        self.interface_id = interface_id
        self.status = status
        self.method = method,
        self.params = params,
        self.url = url,
        self.relation = relation,
        self.relation_params = relation_params,
        self.save_params = save_params,
        self.remarks = remarks
        self.create_time = create_time

    def __str__(self):
        response = {
            "id": self.id,
            "name": self.name,
            "interface": self.interface.__str__(),
            "status": self.status,
            "method": self.method,
            "params": self.params,
            "url": self.url,
            "relation": self.relation,
            "relation_params": self.relation_params,
            "save_params": self.save_params,
            "remarks": self.remarks,
            "create_time": self.create_time
        }
        return response


class Task(db.Model):
    __tablename__ = "task"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", backref="task_of_user")

    case_id = db.Column(db.String(20000), nullable=False)
    interface_id = db.Column(db.String(255), nullable=True)
    project_id = db.Column(db.String(255), nullable=True)

    status = db.Column(db.Integer, nullable=False)
    host = db.Column(db.String(255), nullable=False)
    remarks = db.Column(db.String(255), nullable=True)
    start_time = db.Column(db.DateTime, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, user_id, status, case_id, host, start_time, create_time, remarks, interface_id, project_id):
        self.name = name
        self.user_id = user_id
        self.status = status
        self.case_id = case_id
        self.interface_id = interface_id
        self.project_id = project_id
        self.host = host
        self.remarks = remarks
        self.start_time = start_time
        self.create_time = create_time

    def __str__(self):
        response = {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "status": self.status,
            "case_id": self.case_id,
            "interface_id": self.interface_id,
            "project_id": self.project_id,
            "host": self.host,
            "remarks": self.remarks,
            "start_time": self.start_time,
            "create_time": self.create_time
        }
        return response