#!/usr/bin/python3
import json

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown
from flask_migrate import Migrate

app = Flask(__name__)
with open('/etc/config.json') as config_file:
    config = json.load(config_file)
app.config['SECRET_KEY'] = config.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('SQLALCHEMY_DATABASE_URI')
app.config['RECAPTCHA_USE_SSL'] = True
app.config['RECAPTCHA_PUBLIC_KEY'] = config.get('RECAPTCHA_PUBLIC_KEY')
app.config['RECAPTCHA_PRIVATE_KEY'] = config.get('RECAPTCHA_PRIVATE_KEY')
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'black'}

Markdown(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
from flask_app import routes
