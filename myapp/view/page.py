from . import view_blueprint as main

# 封装了http请求内容
from flask import render_template, url_for, session, request
# 重定向

from .. import db
from datetime import datetime
from .form import nameForm
from .. import bootstrap
from ..sql import bbsUser,bbsuser_all



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
    user_agent = request.headers.get('User-Agent')
    return render_template('about.html', useragent=user_agent)


