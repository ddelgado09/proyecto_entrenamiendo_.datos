import os, sys
from app import create_app, db
from app.models import Usuario
from flask_migrate import Migrate

app = create_app('default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Usuario=Usuario)

@app.cli.command()
def test():
    """ Run the unit tests """

    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)