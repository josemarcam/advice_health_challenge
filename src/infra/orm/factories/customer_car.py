from factory import alchemy, Faker

from src.config.database import db
from src.infra.orm.entities.customers_cars import CustomerCar
from src.domain.customers.models.enums.car_color import CarColorTypes
from src.domain.customers.models.enums.car_type import CarTypes


class CustomerCarFactory(alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = CustomerCar
        sqlalchemy_session = db.session
        # sqlalchemy_session_persistence = "commit"

    color = Faker('random_element', elements=CarColorTypes.as_list())
    type = Faker('random_element', elements=CarTypes.as_list())
    owner = None
