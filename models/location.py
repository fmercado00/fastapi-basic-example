from typing import Optional
from models.city import City

# Pydantic
from pydantic import BaseModel, Field, validator

class Location(BaseModel):
    state: str = Field(
        ...,
        min_length = 1
        )
    city: Optional[City] = Field(
        default=City.LONDON
        )
    country: Optional[str] = Field(
        default = None
        )