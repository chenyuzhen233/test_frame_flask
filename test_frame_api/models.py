from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    # table name
    __tablename__ = "user"
    # table structure
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __str__(self):
        response = {
            "id":self.id,
            "name":self.name
        }
        return response

class Token(db.Model):
    # table name
    __tablename__ = "token"
    # table structure
    id = db.Column(db.Integer, primary_key = True)
    token = db.Column(db.String(10), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    expire_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, token, expire_time):
        self.token = token
        self.expire_time = expire_time


class Project(db.Model):
    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    remarks = db.Column(db.String(255), nullable=True)
    create_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, remarks=None):
        self.name = name
        self.remarks = remarks

    def __str__(self):
        response = {
            "name":self.name,
            "remarks":self.remarks,
            "create_time":self.create_time
        }
        return response


class Module(db.Model):
    __tablename__ = "module"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    project = db.Column(db.Integer, db.ForeignKey('project.id'), )
    remarks = db.Column(db.String(255), nullable=True)
    create_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, project, remarks=None):
        self.name = name
        self.project = project
        self.remarks = remarks

    def __str__(self):
        response = {
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
    module = db.Column(db.Integer, db.ForeignKey('module.id'), )
    remarks = db.Column(db.String(255), nullable=True)
    create_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, module, remarks=None):
        self.name = name
        self.module = module
        self.remarks = remarks

    def __str__(self):
        response = {
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
    interface = db.Column(db.Integer, db.ForeignKey('interface.id'), )
    method = db.Column(db.Integer, nullable=True)
    params = db.Column(db.String(2000), nullable=True)
    url = db.Column(db.String(255), nullable=False)
    relation = db.Column(db.Integer, nullable=False)
    relation_params = db.Column(db.String(2000), nullable=True)
    save_params = db.Column(db.String(2000), nullable=True)

    remarks = db.Column(db.String(255), nullable=True)
    create_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, interface, remarks=None):
        self.name = name
        self.interface = interface
        self.remarks = remarks

    def __str__(self):
        response = {
            "name": self.name,
            "interface": self.interface.__str__(),
            "remarks": self.remarks,
            "create_time": self.create_time
        }
        return response