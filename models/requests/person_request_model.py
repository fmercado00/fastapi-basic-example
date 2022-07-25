from models.person_base import PersonBase
from pydantic import BaseModel, Field, validator, EmailStr



class PersonRequestModel(PersonBase):
    password: str = Field(..., min_length=8)