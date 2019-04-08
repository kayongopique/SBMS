class Config:
    SECRET_KEY = 'hard to guess string'   
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True    
    MAIL_SUBJECT_PREFIX = '[Ireport]'
    MAIL_SENDER = 'kayongopique@gmail.com'
    ADMIN_EMAIL = 'kayongopique@gmail.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG = True
    CSRF_ENABLED = True
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USERNAME ='kayongopique'
    MAIL_PASSWORD = 'bukirwa1994'
    MAIL_USE_TLS =True
    SQLALCHEMY_DATABASE_URI = \
        'postgresql://postgres:david@localhost:5432/flasky'

    

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = \
        'postgresql://postgres:david@localhost:5432/test_flasky'


class ProductionConfig(Config):
    DEBUG =False
    SQLALCHEMY_DATABASE_URI = \
        'postgresql://postgres:david@localhost:5432/prod_flasky'

config = {
    'development': DevConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevConfig
}                   