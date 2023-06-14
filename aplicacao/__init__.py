from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] ='8cb1cb9dcb54cee4d4c123d14c0e9917'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///adopet.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
# login_manager.login_message = 'Realize login para prosseguir'
# login_manager.login_message_category='alert-info'

from aplicacao import routers