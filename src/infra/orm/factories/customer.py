from factory import alchemy, Faker, SubFactory, List
from random import randint

from src.config.database import db
from src.infra.orm.entities.customers import Customer
from src.infra.orm.factories.customer_car import CustomerCarFactory
from src.domain.customers.services.customer_service import CustomerService

class CustomerFactory(alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = Customer
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    name = Faker("name", locale="pt_BR")
    cars = List( SubFactory(CustomerCarFactory) for _ in range(CustomerService.MAX_CARS) )
