from injector import Binder
from flask_injector import request

from src.domain.auth.services import SigninUserService
from src.domain.auth.validators import SigninValidator


def auth_module(binder: Binder):
    
    binder.bind(
        SigninUserService,
        to=SigninUserService,
        scope=request
    )
    binder.bind(
        SigninValidator,
        to=SigninValidator,
        scope=request
    )
 