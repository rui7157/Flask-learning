import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_myapp(app):
        pass


class test(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "Test.sqlite").replace("\\", "/")
    SQLALCHEMY_ON_COMMIT_TEARDOWN=True
    SECRET_KEY = 'hahaha'
    MAIL_SERVER = 'smtp.qq.com' #SMTP这里使用的foxmail
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")  #邮箱从系统环境变量获取
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")  #邮箱密码
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_USERNAME")  #默认的发邮箱


class development(Config):

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "User.sqlite").replace("\\", "/")
    SQLALCHEMY_ON_COMMIT_TEARDOWN=True
    SECRET_KEY = 'hahaha'
    MAIL_SERVER = 'smtp.qq.com' #SMTP这里使用的foxmail
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")  #邮箱从系统环境变量获取
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")  #邮箱密码
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_USERNAME")  #默认的发邮箱


config = {
    'test': test,
    'development': development
}
