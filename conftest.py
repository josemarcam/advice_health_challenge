import pytest
from app import create_app
from faker import Faker

@pytest.fixture
def app():

    app = create_app({
        'TESTING': True,
        'ENV':'TESTING',
        'SQLALCHEMY_DATABASE_URI': 'sqlite://'
    })

    with app.app_context():
        app.db.create_all()

    return app

@pytest.fixture
def faker():
    return Faker(['pt_BR'])
