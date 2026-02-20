from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask(__name__)

app.config['SECRET_KEY']='29a80f465d854c3e00d23fe2870b34146db08cc4'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db=SQLAlchemy(app)

bcrypt=Bcrypt()

login_manager=LoginManager(app)

from flaskblog import routes
