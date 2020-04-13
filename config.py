import os

class Config(object):

    #Base configs
    SECRET_KEY = os.urandom(30)

    #Flask-SQLAlchemy configs.
    SQLALCHEMY_DATABASE_URI = 'postgres://xzjeopdcfcaekz:9a76537746f1fc31998b9973d9df9af64650ad9f2bbbad3885078d3dcb509238@ec2-46-137-84-173.eu-west-1.compute.amazonaws.com:5432/d689rssgarp0p7'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
