from faker import Faker

from src.domain.customers.models.enums.car_color import CarColorTypes
from src.domain.customers.models.enums.car_type import CarTypes
from src.infra.orm.factories.customer import CustomerFactory
from src.infra.orm.factories.customer_car import CustomerCarFactory
from src.infra.orm.factories.user import UserFactory


def get_new_customer(app, batch=0, **kwargs):
    return CustomerFactory.create_batch(batch) if batch > 0 else CustomerFactory(**kwargs)

def get_new_user(app, batch=0, **kwargs):
    return UserFactory.create_batch(batch) if batch > 0 else UserFactory(**kwargs)


def get_new_customer_car(app, customer, batch=0, **kwargs):

    if batch > 0:
        cars = CustomerCarFactory.build_batch(batch, owner=customer, **kwargs)
        for car in cars:
            app.db.session.add(car)
            app.db.session.flush()
            app.db.session.expunge_all()
            app.db.session.commit()
        return cars
    return CustomerCarFactory(owner=customer, **kwargs)

def customer_creation_dict(faker: Faker) -> dict:
    return {
        "name": faker.name()
    }

def customer_car_creation_dict(faker: Faker, customer_id) -> dict:
    return {
        "customer_id": customer_id,
        "color": faker.random_element(CarColorTypes.as_list()),
        "type": faker.random_element(CarTypes.as_list())
    }



