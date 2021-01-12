#!/usr/bin/python3
import json

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
with open('/etc/config.json') as config_file:
    config = json.load(config_file)
app.config['SECRET_KEY'] = config.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
from flask_app import routes
