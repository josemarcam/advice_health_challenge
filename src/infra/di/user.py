from injector import Binder
from flask_injector import request

from src.domain.users.services.user_service import (
    UserService
)
from src.domain.users.repositories.user_repository import (
    UserRepository
    )


def user_module(binder: Binder):
    
    binder.bind(
        UserService,
        to=UserService,
        scope=request
    )

    binder.bind(
        UserRepository,
        to=UserRepository,
        scope=request
    )
