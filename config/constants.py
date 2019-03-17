import os
from os.path import dirname, abspath
import json

from flask_script import Manager

from flask_admin import Admin as FlaskAdmin
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, MigrateCommand

from config.settings import secrets
from . import setup_app, setup_db


BASE_DIR = dirname(dirname(abspath(__file__)))

template_dir = os.path.join(BASE_DIR, 'templates')
static_dir = os.path.join(BASE_DIR, 'static')
secrets_file = os.path.join(BASE_DIR, 'config/secrets.json')

with open(secrets_file) as f:
    secrets = json.loads(f.read())

env_conf = secrets.get('ENVIRONMENT')

app = setup_app(env_conf)
# set template_dir
app.template_folder=template_dir
app.static_folder=static_dir

# database setup
db = setup_db(app)

# register sqlalchemy extension
db.init_app(app)

# external pacakge constants
db_session = db.session
migrate = Migrate(app, db)

# manager settings
manager = Manager(app)
manager.add_command('db', MigrateCommand)

app_admin = FlaskAdmin(app, name='IndiaWyn')
marshmallow = Marshmallow(app)