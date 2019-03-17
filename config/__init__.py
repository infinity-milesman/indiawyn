import os
from pathlib import Path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from .settings import config_by_name


def setup_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    return app

def setup_db(app):
    db = SQLAlchemy(app)
    return db