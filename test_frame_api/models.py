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
            "id":self.id,
            "name":self.name,
            "remarks":self.remarks,
            "create_time":self.create_time
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

    def __init__(self, name, project_id, remarks=None):
        self.name = name
        self.project_id = project_id
        self.remarks = remarks

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

    def __init__(self, name, module_id, remarks=None):
        self.name = name
        self.module_id = module_id
        self.remarks = remarks

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
    method = db.Column(db.Integer, nullable=True)
    params = db.Column(db.String(2000), nullable=True)
    url = db.Column(db.String(255), nullable=False)
    relation = db.Column(db.Integer, nullable=False)
    relation_params = db.Column(db.String(2000), nullable=True)
    save_params = db.Column(db.String(2000), nullable=True)

    remarks = db.Column(db.String(255), nullable=True)
    create_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, interface_id, remarks=None):
        self.name = name
        self.interface_id = interface_id
        self.remarks = remarks

    def __str__(self):
        response = {
            "id": self.id,
            "name": self.name,
            "interface": self.interface.__str__(),
            "remarks": self.remarks,
            "create_time": self.create_time
        }
        return response