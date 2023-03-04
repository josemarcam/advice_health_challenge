from src.config.database import db

class CustomerCar(db.Model):

    __tablename__ = "customers_cars"

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    color = db.Column('color', db.String(8), nullable=False)
    type = db.Column('type', db.String(13), nullable=False)

    customer_id = db.Column('customer_id', db.Integer, db.ForeignKey('customers.id'), nullable=False)
    owner = db.relationship("Customer", back_populates="cars")
    
    created_at = db.Column('created_at', db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column('updated_at', db.DateTime, nullable=False, server_default=db.func.now(), server_onupdate=db.func.now())