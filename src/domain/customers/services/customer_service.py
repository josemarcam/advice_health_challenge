from injector import inject

from src.domain.customers.repositories.customer_repository import CustomerRepository
from src.shared.models.filter_model import ListFilterModel
from src.domain.customers.models.customer_model import (
    CustomerModel, 
    ListCustomerModel,
    CreateCustomerModel, 
)
from src.domain.customers.models.customer_car_model import (
    CustomerCarModel, 
    CreateCustomerCarModel,
)
from src.shared.models.filter_model import ListFilterModel, FilterModel
from src.shared.exceptions import NotFoundException


class CustomerService:

    MAX_CARS = 3
    
    @inject
    def __init__(self, repository: CustomerRepository):
        self._repository = repository

    def get_all_customers(self) -> ListCustomerModel:
        return self._repository.find(None)

    def list_customers_filter(self, list_filters_model: ListFilterModel) -> ListCustomerModel:
        return self._repository.find(list_filters_model)
    
    def create_customer(self, customer_model: CreateCustomerModel) -> CustomerModel:
        return self._repository.create_customer(customer_model)
    
    def create_customer_car(self, create_customer_car_model: CreateCustomerCarModel) -> CustomerCarModel:
        
        car_count_filter = FilterModel(entity_attr="cars_owned", value=CustomerService.MAX_CARS, operation="<")
        customer_id_filter = FilterModel(entity_attr="id", value=int(create_customer_car_model.customer_id), operation="==")
        list_filters_model = ListFilterModel(filters=[car_count_filter, customer_id_filter])
        list_customer = self.list_customers_filter(list_filters_model=list_filters_model)

        if len(list_customer.customers) == 0 or list_customer.customers[0].cars_owned >= CustomerService.MAX_CARS:
            raise NotFoundException("Usuario nao encontrado ou invalido para a operacao")

        return self._repository.create_customer_car(create_customer_car_model)