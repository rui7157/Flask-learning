# -*- utf-8 -*-

'''操作数据'''

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from datetime import datetime
import sqlite3
import os
from . import db
from . import login_manager
basedir = os.path.abspath(os.path.dirname(__file__))


class bbsUser(UserMixin, db.Model):
     #"""用户表存储注册的用户信息"""
    __tablename__ = "bbsusers"
    id = db.Column(db.Integer, primary_key=True)
    Uname = db.Column(db.String(64), nullable=False, index=True, unique=True)
    Upwdhash = db.Column(db.String(16), nullable=False)
    Uemail = db.Column(db.String(64), nullable=False, unique=True)
    Confirmed = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(64))  # 姓名
    localtion = db.Column(db.String(64))  # 地址
    aboutme = db.Column(db.Text)  # 自我介绍
    member_since = db.Column(db.DateTime(), default=datetime.now)  # 注册时间
    last_seen = db.Column(db.DateTime(), default=datetime.now)  # 最后一次登录时间
    Role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def ping(self):
        self.last_seen = datetime.now()
        db.session.add(self)
        db.session.commit()

    def __init__(self,  Uname, Upassword, Uemail):
        self.Uname = Uname
        self.Upwdhash = generate_password_hash(Upassword)
        self.Uemail = Uemail

    def verify_password(self, Upassword):
        return check_password_hash(self.Upwdhash, Upassword)

    def generate_confirmation_token(self, expiration=3600):
        # TimedJSONWebSignatureSerializer
        '''
        dumps() 方法为指定的数据生成一个加密签名，然后再对数据和签名进行序列化，生成令
        牌字符串。 expires_in 参数设置令牌的过期时间，单位为秒。
        loads()这个方法会检验签名和过期时间，如果通过，返回原始数据。如果提供给 loads() 方法的令牌不正
        确或过期了，则抛出异常'''

        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.Confirmed = True
        db.session.add(self)
        db.session.commit()

        return True

    def __repr__(self):
        return '<user %s>' % self.Uname

# 创建一个角色表包含default、permissions列


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    default = db.Column(db.Boolean, default=False)

    permissions = db.Column(db.Integer)
    bbsusers = db.relationship('bbsUser', backref='roles')

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES, True),
            'Moderator': (Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES | Permission.MODERATE_COMMENTS, False),
            'Administrator': (Permission.ADMINISTER, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
                role.permissions = roles[r][0]
                role.default = roles[r][1]
                db.session.add(role)
            db.session.commit()


class Permission:
    '''定义权限常量'''
    FOLLOW = 0x01  # 关注其他用户
    COMMENT = 0x02  # 在他人撰写的文章中发布评论
    WRITE_ARTICLES = 0x04  # 写原创文章
    MODERATE_COMMENTS = 0x08  # 查处他人发表的不当评论
    ADMINISTER = 0x80  # 管理员


def check_db(Upassword, *, Uname, Uemail):
    pass


def read_db(Uname, *, Uemail):
    # 关键字参数，传入参数时候需Uemail=XXX
    if Uname:
        return bbsUser.query.filter_by(Uname=Uname).first()
    else:
        return bbsUser.query.filter_by(Uemail=Uemail).first()


def bbsuser_all():
    return bbsUser.query.all()


@login_manager.user_loader
def loader_user(userid):
    return bbsUser.query.get(userid)
