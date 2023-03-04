from flask import Flask
from flask_jwt_extended import JWTManager

from src.shared.http import Response
from src.domain.users.services.user_service import UserService
from src.domain.auth.models import SignedUserModel
from src.infra.di.user import user_module

def init_app(app: Flask):
    
    jwt = JWTManager(app)

    @jwt.user_lookup_loader
    def current_user(headers, payload) -> SignedUserModel:
        # print(f"aqui no user_service {Injector.}")

        user_service = app.injector.get(UserService)
        return user_service.get_signed_user(payload['sub']['id'])

    @jwt.expired_token_loader
    def expired_refresh_token(jwt_header, jwt_payload):

        msg = "Token de acesso expirado"
        if jwt_payload['type'] == "refresh":
            msg = "refresh token expirado"

        return Response().force_type(Response.UNAUTHORIZED, msg)

        
