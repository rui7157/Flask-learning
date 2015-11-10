from . import view_blueprint as main 
from flask import render_template
from flask import session
from .form import testForm
@main.route('/test')
def test():
	return render_template('test1.html')




