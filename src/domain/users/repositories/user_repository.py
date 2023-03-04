from typing import Union

from src.shared.repositories.base_repository import BaseRepository
from src.domain.users.models.user_model import UserModel
from src.infra.orm.entities.user import User
from src.domain.auth.models import SignedUserModel

class UserRepository(BaseRepository):

    def find_user_by_email(self, email: str) -> Union[UserModel, None]:
            
        user_entity = self.session.scalars(self.db.select(User).filter_by(email=email)).first()
        
        if user_entity:
            return UserModel.from_orm(user_entity)
        
        return None
    
    def find_signed(self, id: str) -> Union[SignedUserModel, None]:
            
        user_entity = self.session.scalars(self.db.select(User).filter_by(id=id)).first()

        if user_entity:
            return SignedUserModel.from_orm(user_entity)
        
        return None