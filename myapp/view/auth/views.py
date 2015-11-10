from . import auth_blueprint as auth
from flask import render_template, flash, redirect, url_for, session, request
from flask.ext.login import login_required, login_user, logout_user
from ...sql import bbsUser, bbsuser_all
from flask.ext.login import current_user
from .form import loginForm, nameForm
from ...other.userre import usernameRe, emailRe
from ... import db
from ..mail import sendMail


@auth.route('/strap')
@login_required
def strap():
    return render_template('strap.html')


@auth.route('/login', methods=['POST', 'GET'])
def login():

    form = loginForm()

    if form.validate_on_submit():
        user = bbsUser.query.filter_by(Uemail=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(url_for('view.new2'))
        flash('用户名或密码错误！')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已经成功退出登录！')
    return redirect(url_for('view.new2'))


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.Confirmed:
        return redirect(url_for('view.new2'))
    if current_user.confirm(token):
        flash('你已经成功验证邮箱，谢谢！')
    else:
        flash('你的验证链接无效或者已经过期！')
    return redirect(url_for('view.new2'))


@auth.route('/register', methods=['POST', 'GET'])
def form():
    name, pwd, email = None, None, None
    form = nameForm()
    if form.validate_on_submit():
        session['name'], session['pwd'], session[
            'email'] = form.name.data, form.pwd.data, form.email.data
        form.pwd.data = ''
        if usernameRe(session['name']).isre() == None or len(session['name']) > 16:
            flash('用户名必需是小于16位的字母或者数字！')
# 判断输入name是否满足other/username_re.py中的re表达式和字符数是否小于16位不满足任何一个则发出flash消息
        elif bbsUser.query.filter_by(Uname=session.get('name')).first() is not None:
            flash('您的用户名已经被注册！')
            form.name.data = ''
# 判断密码是否小于16位
        elif bbsUser.query.filter_by(Uemail=session.get('email')).first() is not None:
            flash('您输入的邮箱已经被注册！')
            form.email.data = ''
# 判断邮箱格式
        else:
            # 符合注册条件写入数据库注册信息
            user = bbsUser(session.get('name'), session.get(
                'pwd'), session.get('email'))
            db.session.add_all([user])
            try:
                db.session.commit()
            except:
                db.session.rollback()
            token = user.generate_confirmation_token(3600)
            auth_url = url_for('auth.confirm', token=token, _external=True)

            sendMail(session.get('email'), session.get('name'),
                     session.get('email'), token=token, auth_url=auth_url)
            login_user(user, True)
            return render_template('register.html', register='ok', form=form, Name=session.get('name'), Pwd=session.get('pwd'), Email=session.get('email'))

        # return redirect(url_for('form'))
# 重定向new1(/form)
    return render_template('register.html', register=None, form=form, Name=session.get('name'), Pwd=session.get('pwd'), Email=session.get('email'))


@auth.before_app_request
def before_request():
    if current_user.is_authenticated:

        current_user.ping()
