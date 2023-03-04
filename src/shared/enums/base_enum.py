from enum import Enum

class BaseEnum(Enum):

    @classmethod
    def as_list(cls) -> list:
        return [e.value for e in cls]