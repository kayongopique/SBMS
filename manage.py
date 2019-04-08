from app import Create_app, db
from flask_migrate import Migrate
from flask_script import Manager
from app.models import Roles
from flask import current_app



app = Create_app('default')
app_context = app.app_context()
app_context.push()
Roles.insert_roles()
db.create_all()
migrate = Migrate(app, db)
manager = Manager(app)


# @manager.command
# def test():

#     '''runs the unit tests'''

#     import unittest
#     test = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == "__main__":
    app.run()


