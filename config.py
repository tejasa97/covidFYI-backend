import os

class Config(object):

    #Base configs
    SECRET_KEY = os.urandom(30)

    #Flask-SQLAlchemy configs.
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost:5432/covid'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
