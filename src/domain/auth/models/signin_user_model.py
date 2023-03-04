from datetime import datetime
from typing import Optional
from pydantic import BaseModel, root_validator

from src.shared.exceptions import ForbiddenException


class SigninUserModel(BaseModel):
    
    email: str
    password: str
    
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

    @root_validator(pre=True)
    def parse_required_fields(cls, values):
        if not values.get("email") or not values.get("password"):
            raise ForbiddenException("Verifique os dados enviados")
        return values
    
class PayloadSigninUserModel(BaseModel):

    user: SigninUserModel
    token: str
    refresh_token: str
