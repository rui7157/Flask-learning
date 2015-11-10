from . import view_blueprint as main 
from flask import render_template

@main.app_errorhandler(404)
def not_foundweb(e):
    return render_template('404.html'),400


