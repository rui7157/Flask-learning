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
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'goodrui@163.com'
    MAIL_PASSWORD = 'a13733431563'


class development(Config):

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "User.sqlite").replace("\\", "/")
    SQLALCHEMY_ON_COMMIT_TEARDOWN=True
    SECRET_KEY = 'hahaha'
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'goodrui@163.com'
    MAIL_PASSWORD = 'a13733431563'
    MAIL_DEFAULT_SENDER = 'goodrui@163.com'


config = {
    'test': test,
    'development': development
}
