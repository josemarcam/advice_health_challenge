from src.shared.validators.base_validator import BaseValidator
from src.domain.customers.models.customer_model import CreateCustomerModel


class CreateCustomerValidator(BaseValidator):

    def __init__(self):
        super().__init__(validator=CreateCustomerModel)
