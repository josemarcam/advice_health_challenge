from pydantic import BaseModel
from typing import Optional

from src.domain.customers.models.enums.car_color import CarColorTypes
from src.domain.customers.models.enums.car_type import CarTypes
    

class CreateCustomerCarModel(BaseModel):
    customer_id: Optional[int] = None
    color: CarColorTypes
    type: CarTypes
    
    class Config:  
        use_enum_values = True

class CustomerCarModel(BaseModel):
    id: int
    color: CarColorTypes
    type: CarTypes
    customer_id: int

    class Config:
        orm_mode = True
        use_enum_values = True
