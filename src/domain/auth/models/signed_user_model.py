from pydantic import BaseModel


class SignedUserModel(BaseModel):

    id: int
    email: str

    class Config:
        orm_mode=True