from flask_jwt_extended.utils import create_refresh_token
from injector import inject
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from datetime import timedelta



from src.shared.exceptions import (
    UnauthorizedException
)
from src.domain.auth.models import (
    SigninUserModel,
    PayloadSigninUserModel
)

from src.domain.users.repositories.user_repository import UserRepository

class SigninUserService:

    EXPIRES_TOKEN = 1
    EXPIRES_REFRESH_TOKEN = 2
    
    @inject
    def __init__(self, repository: UserRepository ):
        self._repository = repository        
    
    def signin(self, credentials: SigninUserModel) -> PayloadSigninUserModel:
        
        payload = self._signin(credentials)

        return payload

    def get_fresh_token(self,user: SigninUserModel) -> PayloadSigninUserModel:
        
        user = self._repository.find_user_by_email(email=user.email)
        payload = self._get_token(user,id=user.id)
        
        return payload

    def _signin(self, credentials: SigninUserModel) -> PayloadSigninUserModel:
        
        user = self._repository.find_user_by_email(email=credentials.email)
        if not user:
            raise UnauthorizedException("Usuário ou senha incorretos")
        
        password_confirmed = check_password_hash(user.password, credentials.password) 
        if not password_confirmed:
            raise UnauthorizedException("Usuário ou senha incorretos")
        
        payload = self._get_token(user, id=user.id)

        return payload
    
    def _get_token(self,user,**kwargs):
        
        token = create_access_token(kwargs, expires_delta=timedelta(days=self.EXPIRES_TOKEN))
        refresh_token = create_refresh_token(kwargs, expires_delta=timedelta(days=self.EXPIRES_REFRESH_TOKEN))
        payload = PayloadSigninUserModel(user=user, token=token, refresh_token=refresh_token)
        return payload
