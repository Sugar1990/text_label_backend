from app.conf import PG_DB_SERVER_IP, PG_DB_PORT, PG_DB_NAME, PG_USER_NAME, PG_USER_PASSWORD

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '0YmDFVzVXy2X2bv0rQxGD3qi3J71JLMePR+IJL9T'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    JSON_SORT_KEYS = False
    RESTFUL_JSON = dict(ensure_ascii=False)

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'postgresql://%s:%s@%s:%s/%s' % (
                                  PG_USER_NAME, PG_USER_PASSWORD, PG_DB_SERVER_IP, PG_DB_PORT, PG_DB_NAME)


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
