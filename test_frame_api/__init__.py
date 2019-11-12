from flask import Flask, request
from .models import db
from .utils.config import config

host = config.get("database", "host")
port = config.get("database", "port")
user_name = config.get("database", "user_name")
password = config.get("database", "password")
db_name = config.get("database", "db_name")

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://test:a123456@localhost:3306/test_robot"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://%s:%s@%s:%s/%s" % (user_name,
                                                                            password,
                                                                            host,
                                                                            port,
                                                                            db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)


from .views import user
from .views import case
from .views import project
from .views import module
from .views import interface
from .views import login
from .views import task
