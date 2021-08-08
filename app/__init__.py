from flask import Flask
from config import config

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from . import views
    views.init_app(app)
    db.init_app(app)

    return app
