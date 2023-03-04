from flask import Blueprint, request
from injector import inject
from flask_jwt_extended import jwt_required

from src.shared.http import Response
from src.domain.customers.services.customer_service import CustomerService
from src.shared.models.filter_model import ListFilterModel, FilterModel
from src.domain.customers.validators import CreateCustomerValidator, CreateCustomerCarValidator
from src.domain.customers.models.customer_model import CreateCustomerModel
from src.domain.customers.models.customer_car_model import CreateCustomerCarModel


customer_bp = Blueprint("customer", __name__, url_prefix="/api/customers")

@customer_bp.route('/', methods=['GET'])
@jwt_required()
@inject
def get_all_customers(service: CustomerService):

    payload = service.get_all_customers()

    return Response().force_type(Response.OK, "", payload.dict())

@customer_bp.route('/able_to_buy', methods=['GET'])
@jwt_required()
@inject
def get_able_to_buy_customers(service: CustomerService):

    filter = FilterModel(entity_attr="cars_owned", value=int(CustomerService.MAX_CARS), operation="<")
    list_filters_model = ListFilterModel(filters=[filter])
    payload = service.list_customers_filter(list_filters_model=list_filters_model)
    return Response().force_type(Response.OK, "", payload.dict())

@customer_bp.route('/', methods=['POST'])
@jwt_required()
@inject
def create_customer(service: CustomerService, validator: CreateCustomerValidator):

    request_data = request.get_json()
    if not validator.is_valid(request_data):
        return Response().force_type(Response.UNPROCESSABLE_ENTITY, "Verifique os dados enviados", validator.errors)

    create_customer_model = CreateCustomerModel(**request_data)
    customer_model = service.create_customer(create_customer_model)
    return Response().force_type(Response.OK, "", customer_model.dict())

@customer_bp.route('/<int:customer_id>/cars', methods=['POST'])
@jwt_required()
@inject
def create_customer_car(customer_id: int, service: CustomerService, validator: CreateCustomerCarValidator):

    request_data = request.get_json()
    if not validator.is_valid(request_data):
        return Response().force_type(Response.UNPROCESSABLE_ENTITY, "Verifique os dados enviados", validator.errors)
    
    request_data["customer_id"] = customer_id
    create_customer_car_model = CreateCustomerCarModel(**request_data)
    customer_model = service.create_customer_car(create_customer_car_model)
    print(customer_model)
    return Response().force_type(Response.OK, "Carro Registrado com sucesso", customer_model.dict())