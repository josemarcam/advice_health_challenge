from injector import Binder
from flask import Flask
from flask_injector import FlaskInjector, singleton
from flask_sqlalchemy import SQLAlchemy

from src.config.database import db
from src.infra.di import (
    auth_module,
    user_module,
    customer_module
    
)

def init_app(app: Flask):

    def application_module(binder: Binder):
        binder.bind(
            SQLAlchemy,
            to=db,
            scope=singleton,
        )

    return FlaskInjector(app=app, modules=[
        application_module,
        auth_module,
        user_module,
        customer_module
        
    ]).injector
