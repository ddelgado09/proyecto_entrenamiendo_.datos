import os, json
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'proyecto_entrenamiento_paz_uan'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOST = ""
    USER = ""
    PASSWORD = ""
    DB = ""

    def __init__(self):
        with open('db_credentials.json') as json_file:
            data = json.load(json_file)
            self.HOST = data['host']
            self.USER = data['user']
            self.PASSWORD = data['password']
            self.DB = data['db']

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    cnf = Config()
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
        'postgresql://' + cnf.USER + ':' + cnf.PASSWORD + '@' + cnf.HOST + '/' + cnf.DB

class TestingConfig(Config):
    cnf = Config()
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
        'postgresql://' + cnf.USER + ':' + cnf.PASSWORD + '@' + cnf.HOST + '/' + cnf.DB

class ProductionConfig(Config):
    cnf = Config()
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
        'postgresql://' + cnf.USER + ':' + cnf.PASSWORD + '@' + cnf.HOST + '/' + cnf.DB

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}