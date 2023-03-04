from flask import Blueprint, request, current_app
from datetime import datetime
from injector import inject
from flask_jwt_extended import jwt_required, get_current_user

from src.shared.http import Response
from src.domain.auth.validators import SigninValidator
from src.domain.auth.models import SigninUserModel
from src.domain.auth.services import SigninUserService


auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route('/signin', methods=['POST'])
@inject
def signin(service: SigninUserService, validator: SigninValidator):

    request_data = request.get_json()
    if not validator.is_valid(request_data):
        return Response().force_type(Response.UNPROCESSABLE_ENTITY, "Verifique os dados enviados", validator.errors)

    credentials = SigninUserModel(**request_data)
    payload = service.signin(credentials)

    return Response().force_type(Response.OK, "Usuário autenticado", payload.dict())

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
@inject
def get_fresh_token(service: SigninUserService):
    user = get_current_user()
    payload = service.get_fresh_token(user = user)
    return Response().force_type(Response.OK, "Usuário autenticado", payload.dict())
