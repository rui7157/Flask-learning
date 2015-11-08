from myapp import create_app, db
from flask.ext.script import Manager, Shell
from flask.ext.migrate import MigrateCommand
from myapp.sql import Role

app = create_app('development')
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def run(): 
    app.run(debug=True)


@manager.command
def create_db():
    db.create_app()


@manager.command
def test():

    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
