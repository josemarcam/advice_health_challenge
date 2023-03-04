from src.shared.validators.base_validator import BaseValidator
from src.domain.auth.models.signin_user_model import SigninUserModel


class SigninValidator(BaseValidator):

    def __init__(self):
        super().__init__(validator=SigninUserModel)
