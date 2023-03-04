from flask import Flask
from flask_migrate import Migrate

from src import config
from src.config import database, views, di, jwt, exceptions
from src.config.database import db


def create_app(runtime_config: dict = None) -> Flask:
        
    app = Flask(__name__)
    config.init_app(app, runtime_config)
    database.init_app(app)
    views.init_app(app)
    exceptions.init_app(app)
    jwt.init_app(app)
    migrate = Migrate(app, db)
    injector = di.init_app(app)
    app.injector = injector

    return app
