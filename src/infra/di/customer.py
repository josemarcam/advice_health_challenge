from injector import Binder
from flask_injector import request

from src.domain.customers.services.customer_service import (
    CustomerService
)
from src.domain.customers.repositories.customer_repository import (
    CustomerRepository
)
from src.domain.customers.validators import CreateCustomerValidator


def customer_module(binder: Binder):
    
    binder.bind(
        CustomerService,
        to=CustomerService,
        scope=request
    )
    binder.bind(
        CustomerRepository,
        to=CustomerRepository,
        scope=request
    )
    binder.bind(
        CreateCustomerValidator,
        to=CreateCustomerValidator,
        scope=request
    )
