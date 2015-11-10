#conding:utf-8
from flask.ext.mail import Mail, Message
from .. import mail


def sendMail(rev,username,email,token,auth_url):
    msg = Message('hello %s!' %username, recipients=[rev])
    msg.title='this is test mail'
    msg.body = 'thank you register we,your username is %s and Email is %s,please check that is yourself send the Email!' %(username,email)
    msg.html = "<b>thank you register we,your username is %s and Email is %s,please check that is yourself send the Email! </b></br><b>%s</b>"%(username,email,auth_url)
    mail.send(msg)
