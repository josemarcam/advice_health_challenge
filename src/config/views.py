from flask import Flask

from src.infra.views.auth import auth_bp
from src.infra.views.customer import customer_bp

def init_app(app: Flask):
    app.register_blueprint(auth_bp)
    app.register_blueprint(customer_bp)
    