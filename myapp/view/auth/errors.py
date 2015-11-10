from . import auth_blueprint as auth
from flask import render_template

@auth.app_errorhandler(401)
def not_auth(e):
	return render_template('auth/401.html'),401