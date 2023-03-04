from factory import alchemy, Faker
from werkzeug.security import generate_password_hash

from src.config.database import db
from src.infra.orm.entities.user import User


class UserFactory(alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = User
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    email = Faker('email')
    password = generate_password_hash('123qwe', salt_length=10)
