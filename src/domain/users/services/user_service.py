from injector import inject

from src.domain.users.repositories.user_repository import UserRepository
from src.shared.exceptions import NotFoundException

class UserService:

    @inject
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def get_signed_user(self, id: int) :
        signed_user_model = self._repository.find_signed(id)
        if signed_user_model:
            return signed_user_model

        raise NotFoundException