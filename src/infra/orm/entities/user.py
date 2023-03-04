from src.config.database import db

class User(db.Model):

    __tablename__ = "users"

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    email = db.Column('email', db.String(120), nullable=False, unique=True)
    password = db.Column('password', db.String(255), nullable=False)
    
    created_at = db.Column('created_at', db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column('updated_at', db.DateTime, nullable=False, server_default=db.func.now(), server_onupdate=db.func.now())