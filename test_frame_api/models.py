from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    # table name
    __tablename__ = "user"
    # table structure
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        response = {
            "id":self.id,
            "name":self.name
        }

class Token(db.Model):
    # table name
    __tablename__ = "token"
    # table structure
    id = db.Column(db.Integer, primary_key = True)
    token = db.Column(db.String(10), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    expire_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token