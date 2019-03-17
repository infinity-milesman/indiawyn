import os
from os.path import dirname, abspath
import json

BASE_DIR = dirname(dirname(abspath(__file__)))
SECRETS_FILE = os.path.join(BASE_DIR, 'config/secrets.json')

if os.path.exists(SECRETS_FILE) is False:
    raise Exception(" Please add 'secrets.json' file in config/ folder.")

with open(SECRETS_FILE) as f:
    secrets = json.loads(f.read())

# default settings
DEFAULT_SERVER_PORT = secrets.get('SERVER_PORT', 8080)
DEFAULT_SERVER_HOST = secrets.get('SERVER_HOST', 'localhost')

# default database settings
DATABASE_ENGINE = secrets.get('DATABASE_ENGINE')
DATABASES = {
    'postgresql': {
        'ENGINE': 'postgresql',
        'NAME': secrets.get('DB_NAME'),
        'USERNAE': secrets.get('DB_USER'),
        'PASSWORD': secrets.get('DB_PASSWORD'),
        'HOST': secrets.get('DB_HOST'),
        'PORT': secrets.get('DB_PORT'),
        'DATABASE_URI': "postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}".format(
            db_username=secrets.get('DB_USERNAME'),
            db_password=secrets.get('DB_PASSWORD'),
            db_host=secrets.get('DB_HOST'),
            db_port=secrets.get('DB_PORT'),
            db_name=secrets.get('DB_NAME'),
        )
    }
}


class Config:
    SECRET_KEY = secrets.get('SECRET_KEY', 'my_precious_secret_key')
    SERVER_PORT = DEFAULT_SERVER_PORT
    SERVER_HOST = DEFAULT_SERVER_HOST
    UPLOAD_FOLDER = secrets.get('UPLOAD_FOLDER')
    ALLOWED_EXTENSIONS = secrets.get('ALLOWED_EXTENSIONS')
    DEBUG = False


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = DATABASES.get(DATABASE_ENGINE).get('DATABASE_URI')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secrets.get('SECRET_KEY')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class TestingConfig(Config):
    ENV = 'testing'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = DATABASES.get(DATABASE_ENGINE).get('DATABASE_URI')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secrets.get('SECRET_KEY')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = DATABASES.get(DATABASE_ENGINE).get('DATABASE_URI')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secrets.get('SECRET_KEY')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


config_by_name = dict(
    DEVELOPMENT=DevelopmentConfig,
    TESTING=TestingConfig,
    PRODUCTION=ProductionConfig
)
