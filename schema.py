from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    NON_BINARY = "non-binary"
    OTHER = "other"


class Persona(BaseModel):
    alias: str
    gender: Gender

