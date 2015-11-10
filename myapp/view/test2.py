# -*- coding:utf-8 -*-
from config import config
from flask import Flask
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.blueprint import Blueprint
from flask.ext.mail import Mail
moment = Moment()
db = SQLAlchemy()
bapp=Blueprint('main',__name__)
defind=deFlask(__name__)
def create_app(config_name):
	print (Flask)
	app=Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_myapp(app)
	mail=Mail(defind)
	moment.init_app(app)
	db.init_app(app)
	print ('config[config_name] is:',config[config_name])
	print ('moment is:',moment)
	print ('mail is:',mail)
	print ('db is:',db)
	print ('The name is:',__name__)
	return app

# app = Flask(__name__)
# app.config.from_object(config[config_name])
# config[config_name].init_app(app)