# -*- coding:utf-8 -*-
from flask import Flask, render_template, url_for, session
# 导入模版，反向url
from flask.ext.login import current_user
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

# 时间
import jinja2
# jinja2模板框架
from .other.userre import usernameRe, emailRe
from flask.ext.sqlalchemy import SQLAlchemy
# 数据库
from sqlalchemy import Column, String, create_engine
from flask.ext.migrate import Migrate,MigrateCommand
from flask.ext.script import Manager
from flask.ext.mail import Mail
from config import config 
import sqlite3
import os.path
from flask import Blueprint
from flask.ext.login import LoginManager
CSRF_ENABLED = True


mail = Mail()
bootstrap = Bootstrap()
db=SQLAlchemy()
login_manager=LoginManager()
# login_manager.login_view='auth.login'  #

def create_app(config_name):
	
	app=Flask(__name__)
	
	app.config.from_object(config[config_name])

	mail.init_app(app)
	bootstrap.init_app(app)
	login_manager.init_app(app)
	db.init_app(app)
	migrate = Migrate(app,db)
	from .view import view_blueprint
	app.register_blueprint(view_blueprint)
	from .view.auth import auth_blueprint
	app.register_blueprint(auth_blueprint,url_prefix='/auth')
	from .view.users import users_blueprint
	app.register_blueprint(users_blueprint,user_prefix='/users')

	return app





