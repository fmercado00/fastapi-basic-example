
from pydantic import BaseModel, Field, validator, EmailStr
from models.person_base import PersonBase


class PersonResponseModel(PersonBase):
    pass
    # @validator('email')
    # def validate_email(cls, v):
    #     if not v.endswith('@domain.com'):
    #         raise ValueError('Email must be a gmail address')
    #     return v

   