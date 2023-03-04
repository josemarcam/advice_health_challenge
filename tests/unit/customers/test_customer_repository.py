from tests.fixtures import get_new_customer, customer_creation_dict, customer_car_creation_dict
from src.domain.customers.repositories.customer_repository import CustomerRepository
from src.shared.models.filter_model import FilterModel, ListFilterModel
from src.domain.customers.models.customer_model import CreateCustomerModel
from src.domain.customers.models.customer_car_model import CreateCustomerCarModel

def test_find_customer(app):
    
    repository: CustomerRepository = app.injector.get(CustomerRepository)
    
    customer = get_new_customer(app)
    list_customers = repository.find()

    assert list_customers.customers[0].id == customer.id

    filter = FilterModel(entity_attr="id", value=customer.id, operation="==")
    list_filters = ListFilterModel(filters=[filter])

    list_customers = repository.find(list_filters)

    assert list_customers.customers[0].id == customer.id

def test_create_customer(app, faker):

    repository: CustomerRepository = app.injector.get(CustomerRepository)
    
    create_customer_model = CreateCustomerModel(**customer_creation_dict(faker))
    customer_model = repository.create_customer(create_customer_model)

    assert customer_model.name == create_customer_model.name

def test_create_customer_car(app, faker):

    repository: CustomerRepository = app.injector.get(CustomerRepository)
    
    customer = get_new_customer(app)
    create_customer_car_model = CreateCustomerCarModel(**customer_car_creation_dict(faker, customer.id))
    
    customer_car_model = repository.create_customer_car(create_customer_car_model)

    assert customer_car_model.color == create_customer_car_model.color
    assert customer_car_model.customer_id == create_customer_car_model.customer_id

    