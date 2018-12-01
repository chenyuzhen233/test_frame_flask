from flask import Flask, request
from models import db,User,Token

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://test:a123456@localhost:3306/test_robot"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)


from .views import user
from .views import case
from .views import project
from .views import module
from .views import interface