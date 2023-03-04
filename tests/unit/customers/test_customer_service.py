import pytest

from tests.fixtures import get_new_customer, get_new_customer_car, customer_car_creation_dict, customer_creation_dict
from src.domain.customers.services.customer_service import CustomerService
from src.shared.models.filter_model import FilterModel, ListFilterModel
from src.domain.customers.models.customer_model import CreateCustomerModel

from src.domain.customers.models.customer_car_model import CreateCustomerCarModel
from src.shared.exceptions import NotFoundException



def test_get_list_customer(app):
    customers = get_new_customer(app, 3)
    service : CustomerService = app.injector.get(CustomerService)
    found_model = service.get_all_customers()

    for found, customer in zip(found_model.customers, customers):
        assert found.id == customer.id

def test_get_list_customer_with_filter(app):
    filter = FilterModel(entity_attr="id", value=1, operation="==")
    filter_list = ListFilterModel(filters=[filter])
    
    customers = get_new_customer(app, 3)
    service : CustomerService = app.injector.get(CustomerService)
    found_model = service.list_customers_filter(filter_list)
    assert len(found_model.customers) == 1
    assert found_model.customers[0].id == customers[0].id

def test_create_customer(app, faker):
    customer_dict = customer_creation_dict(faker)
    create_customer_model = CreateCustomerModel(**customer_dict)
    service : CustomerService = app.injector.get(CustomerService)
    customer_model = service.create_customer(create_customer_model)
    assert customer_model.name == customer_dict.get("name")

def test_create_customer_car(app, faker):
    
    customer = get_new_customer(app, cars=[])
    
    create_customer_car_dict = customer_car_creation_dict(faker, customer.id)
    create_customer_model = CreateCustomerCarModel(**create_customer_car_dict)
    
    service : CustomerService = app.injector.get(CustomerService)
    customer_model = service.create_customer_car(create_customer_model)

    assert customer_model.color == create_customer_car_dict.get("color")

def test_create_customer_car_with_invalid_customer(app, faker):
    
    customer = get_new_customer(app)
    
    create_customer_car_dict = customer_car_creation_dict(faker, 2)
    create_customer_model = CreateCustomerCarModel(**create_customer_car_dict)
    
    service : CustomerService = app.injector.get(CustomerService)
    with pytest.raises(NotFoundException):
        customer_model = service.create_customer_car(create_customer_model)

def test_create_customer_car_with_customer_max_cars(app, faker):
    
    service : CustomerService = app.injector.get(CustomerService)
    
    customer = get_new_customer(app)
    customer_cars = get_new_customer_car(app, customer, service.MAX_CARS)
    # print(customer.cars)
    # print(customer_cars)
    create_customer_car_dict = customer_car_creation_dict(faker, customer.id)
    create_customer_model = CreateCustomerCarModel(**create_customer_car_dict)
    
    service : CustomerService = app.injector.get(CustomerService)
    with pytest.raises(NotFoundException):
        customer_model = service.create_customer_car(create_customer_model)