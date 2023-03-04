from pydantic import BaseModel
from typing import List, Optional

from src.domain.customers.models.enums.car_color import CarColorTypes
from src.domain.customers.models.enums.car_type import CarTypes


class CustomerCarsModel(BaseModel):
    
    id: int
    color: CarColorTypes
    type: CarTypes
    
    class Config:
        orm_mode = True
        use_enum_values = True

class CustomerModel(BaseModel):

    id: int
    name: str
    cars_owned: int
    cars: List[CustomerCarsModel]

    class Config:
        orm_mode = True
    
class ListCustomerModel(BaseModel):
    
    customers: Optional[List[CustomerModel]] = []

    class Config:
        orm_mode = True

class CreateCustomerModel(BaseModel):

    name: str