from pydantic import BaseModel
from typing import Union, List


class FilterModel(BaseModel):
    
    entity_attr: str
    value: Union[str, int]
    operation: str

class ListFilterModel(BaseModel):
    filters: List[FilterModel]