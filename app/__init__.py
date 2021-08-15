from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from . import views, jobs
    views.init_app(app)
    db.init_app(app)
    # jobs.init_app(app)

    return app
