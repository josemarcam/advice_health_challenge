from typing import Union, List
from sqlalchemy import and_
from sqlalchemy.orm import joinedload

from src.shared.repositories.base_repository import BaseRepository
from src.infra.orm.entities.customers import Customer, CustomerCar
from src.domain.customers.models.customer_model import (
    CustomerModel,
    ListCustomerModel, 
    CreateCustomerModel,
    )
from src.domain.customers.models.customer_car_model import (
    CustomerCarModel,
    CreateCustomerCarModel, 
)
from src.shared.models.filter_model import ListFilterModel


class CustomerRepository(BaseRepository):

    def find(self, list_filters_model: Union[ListFilterModel, None] = None) -> Union[ListCustomerModel, List[None]]:
        
        filter_list = []
        if list_filters_model:
            filter_list = self.format_filters(list_filters_model, Customer)

        customer_entities = self.session.query(Customer).\
            options(joinedload(Customer.cars)).\
            filter(and_(True, *filter_list)).all()
        
        return ListCustomerModel(customers=customer_entities)
    
    def create_customer(self, customer_model: CreateCustomerModel) -> CustomerModel:

        customer_entity = Customer(cars=[])
        for customer_model_field in list(customer_model.dict().keys()):
            setattr(customer_entity, customer_model_field, getattr(customer_model, customer_model_field))
        self.model = customer_entity
        self.save()

        return CustomerModel.from_orm(self.model)
    
    def create_customer_car(self, customer_car_model: CreateCustomerCarModel) -> CustomerCarModel:

        customer_entity = CustomerCar()
        for customer_car_model_field in list(customer_car_model.dict().keys()):
            setattr(customer_entity, customer_car_model_field, getattr(customer_car_model, customer_car_model_field))
        self.model = customer_entity
        self.save()

        return CustomerCarModel.from_orm(self.model)


