import os

class BaseConfig(object):
    DEBUG  = False
    TESTING = False
    SECRET_KEY = os.urandom(16)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class ProductionConfig(BaseConfig):
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'  
    SQLALCHEMY_POOL_RECYCLE = 60
    SQLALCHEMY_POOL_PRE_PING = True
    SQLALCHEMY_POOL_SIZE = 1000
    SQLALCHEMY_MAX_OVERFLOW = 2000
    SQLALCHEMY_POOL_TIMEOUT = 30