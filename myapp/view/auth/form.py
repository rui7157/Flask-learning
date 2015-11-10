from flask.ext.wtf import Form
# 表单导入
from wtforms import StringField, SubmitField, PasswordField, BooleanField
# 表单元素：文本字段、提交按钮、密码字段、单选框
from wtforms.validators import DataRequired, Email, Required, Length,EqualTo



class nameForm(Form):
    name = StringField('用户名', validators=[DataRequired(), Length(4,16,'用户名必需是小于16位的字母或者数字！')])
    email = StringField('电子邮箱', validators=[DataRequired(),Email('请输入正确的Email地址')])
    pwd = PasswordField('密码', validators=[DataRequired(), Length(4,16,'密码必须是长度必须是6~16位的字母或数字！'),EqualTo('pwd2','两次密码必需一样')])
    pwd2 = PasswordField('确认密码', validators=[DataRequired()])

    remenber_me = BooleanField('记住我', default=False)
    submit = SubmitField('确认注册')


class loginForm(Form):
	email=StringField('Email', validators=[DataRequired(),Email('请输入正确的邮箱地址')])
	password=PasswordField('密码',validators=[Required('密码不能为空')])
	remember_me=BooleanField('记住登录')
	subm=SubmitField('登录')
