import os
from dotenv import load_dotenv
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    APP_NAME = 'Lotoes Master'

    SECRET_KEY = os.getenv('SECRET_KEY', default='')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ITEMS_PER_PAGE = 25
    #DOMAINS = ['localhost', '']
    MAIL_SERVER = os.getenv('MAIL_SERVER', default='')
    MAIL_PORT = os.getenv('MAIL_PORT', default='')
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', default='')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', default='')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME', default='')
    MAIL_ASCII_ATTACHMENTS = True

    LOTOES_MAIL_SEND = os.getenv('LOTOES_MAIL_SEND', default='')
    LOTOES_MAIL_FROM = os.getenv('LOTOES_MAIL_FROM', default='')

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')


class TestConfig(DevConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')


config = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig,
    'default': DevConfig
}