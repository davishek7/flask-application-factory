from flask import Flask
from .extentions import db, migrate
from os import environ


def get_settings():
    return environ.get('SETTINGS')

def create_app():

    app = Flask(__name__)

    app.config.from_object(get_settings())

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    from .task import task

    app.register_blueprint(task, url_prefix = '/')

    return app