from src.shared.validators.base_validator import BaseValidator
from src.domain.customers.models.customer_car_model import CreateCustomerCarModel


class CreateCustomerCarValidator(BaseValidator):

    def __init__(self):
        super().__init__(validator=CreateCustomerCarModel)
