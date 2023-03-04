from pydantic import BaseModel
from datetime import datetime

class UserModel(BaseModel):

    id: int
    email: str
    password: str
    
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True