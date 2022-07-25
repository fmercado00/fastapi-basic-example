# Pydantic
from pydantic import BaseModel, Field, validator, EmailStr

class LoginResponseModel(BaseModel):
    username: str = Field(..., max_length=40, example="pacousracc2022")
    message: str = Field(default="Login Successful")
