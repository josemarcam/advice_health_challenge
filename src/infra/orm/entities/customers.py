from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import select, func
from sqlalchemy.orm import column_property

from src.config.database import db
from src.infra.orm.entities.customers_cars import CustomerCar

class Customer(db.Model):

    __tablename__ = "customers"

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("name", db.String(255), nullable=False)

    cars = db.relationship("CustomerCar", back_populates="owner")

    created_at = db.Column('created_at', db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column('updated_at', db.DateTime, nullable=False, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, cars, **kwargs):
        super().__init__(**kwargs)
        self.cars = cars
    
    @hybrid_property
    def cars_owned(self):
        return len(self.cars)
    
    @cars_owned.expression
    def cars_owned(cls):
        return select(func.count(CustomerCar.id )).\
            where(CustomerCar.customer_id == cls.id).\
            scalar_subquery()