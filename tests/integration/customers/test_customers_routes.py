from flask_jwt_extended import create_access_token
from http import HTTPStatus

from tests.fixtures import get_new_user, get_new_customer, customer_creation_dict, customer_car_creation_dict

def test_get_all_customers(app):

    customer = get_new_customer(app)

    user = get_new_user(app)
    jwt_token = create_access_token({"id": user.id})

    with app.test_client() as client:
        with app.app_context():
            rv = client.get("/api/customers/", headers={'Authorization': f'Bearer {jwt_token}'})
    assert rv.get_json().get('data', {}).get('customers', {})[0].get('id', 0) == customer.id

def test_get_able_to_buy_customers(app):

    customer = get_new_customer(app, cars=[])

    user = get_new_user(app)
    jwt_token = create_access_token({"id": user.id})

    with app.test_client() as client:
        with app.app_context():
            rv = client.get("/api/customers/able_to_buy", headers={'Authorization': f'Bearer {jwt_token}'})
    assert rv.get_json().get('data', {}).get('customers', {})[0].get('id', 0) == customer.id

def test_create_customer(app, faker):

    create_customer_dict = customer_creation_dict(faker)
    user = get_new_user(app)
    jwt_token = create_access_token({"id": user.id})

    with app.test_client() as client:
        with app.app_context():
            rv = client.post("/api/customers/", headers={'Authorization': f'Bearer {jwt_token}'}, json=create_customer_dict)
    assert rv.get_json().get('data', {}).get('name', {}) == create_customer_dict.get("name")

def test_create_customer_car(app, faker):

    customer = get_new_customer(app, cars=[])
    create_customer_car_dict = customer_car_creation_dict(faker, customer_id=customer.id)
    
    user = get_new_user(app)
    jwt_token = create_access_token({"id": user.id})

    with app.test_client() as client:
        with app.app_context():
            rv = client.post(f"/api/customers/{customer.id}/cars", headers={'Authorization': f'Bearer {jwt_token}'}, json=create_customer_car_dict)
    assert rv.get_json().get('data', {}).get('color', {}) == create_customer_car_dict.get("color")


def test_create_customer_car_with_invalid_user(app, faker):

    customer = get_new_customer(app, cars=[])
    create_customer_car_dict = customer_car_creation_dict(faker, customer_id=customer.id)
    
    user = get_new_user(app)
    jwt_token = create_access_token({"id": user.id})

    with app.test_client() as client:
        with app.app_context():
            rv = client.post(f"/api/customers/3/cars", headers={'Authorization': f'Bearer {jwt_token}'}, json=create_customer_car_dict)
    
    assert rv.status_code == HTTPStatus.NOT_FOUND
    assert rv.get_json().get("message") == "Usuario nao encontrado ou invalido para a operacao"

def test_create_customer_car_with_max_cars(app, faker):

    customer = get_new_customer(app)
    create_customer_car_dict = customer_car_creation_dict(faker, customer_id=customer.id)
    
    user = get_new_user(app)
    jwt_token = create_access_token({"id": user.id})

    with app.test_client() as client:
        with app.app_context():
            rv = client.post(f"/api/customers/{customer.id}/cars", headers={'Authorization': f'Bearer {jwt_token}'}, json=create_customer_car_dict)
    
    assert rv.status_code == HTTPStatus.NOT_FOUND
    assert rv.get_json().get("message") == "Usuario nao encontrado ou invalido para a operacao"
