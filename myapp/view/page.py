from . import view_blueprint as main

# 封装了http请求内容
from flask import render_template, url_for, session, request,abort
# 重定向
from flask.ext.login import login_required, login_user, logout_user,current_user
from .. import db
from datetime import datetime
from .form import nameForm
from .. import bootstrap
from ..sql import bbsUser, bbsuser_all


@main.route('/blog')
def blog():

    return render_template('blog.html', now_time=datetime.utcnow(), main=main, bbsuser_all=bbsuser_all())


@main.route('/boot')
def ext_wtf():

    return render_template('ext_bootstrap.html', now_time=datetime.utcnow())

@main.route('/')
def new2():
    return render_template('index.html')


@main.route('/about')
def user_agents():
    send_email = False
    user_agent = request.headers.get('User-Agent')
    if current_user.is_authenticated and current_user.Confirmed == 0:

        send_email = True

    return render_template('about.html', useragent=user_agent, send_email=send_email)

@main.route('/user/<Uname>')
def user(Uname):
	user=bbsUser.query.filter_by(Uname=Uname).first()
	if user is None:
		abort(404)
	return render_template('user.html',user=user)
