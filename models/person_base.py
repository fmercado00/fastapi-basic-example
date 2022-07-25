
# Python
from distutils.command.config import config
import email
from enum import Enum
from turtle import title
from typing import Optional
from models.city import City

# Pydantic
from pydantic import BaseModel, Field, validator, EmailStr

class PersonBase(BaseModel):
    name: str = Field(
        ..., 
        min_length=1,
        max_length=250,
        example="John Doe"
        )
    age: int = Field(
        ...,
        gt=0, 
        le=115, 
        example=25
        )
    email: EmailStr = Field(
        ...,
        example="somebody@domain.com",
        title="Email",
        description="The email of the person that will receive the message.",
    )
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[City] = Field(
        default=City.LONDON
        )
    state: Optional[str] = None
    zip: Optional[str] = None
    country: Optional[str] = None
    company: Optional[str] = None
    position: Optional[str] = None
    website: Optional[str] = None
    twitter: Optional[str] = None
    facebook: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    instagram: Optional[str] = None
    youtube: Optional[str] = None
    tumblr: Optional[str] = None
    pinterest: Optional[str] = None
    quora: Optional[str] = None
    stackoverflow: Optional[str] = None
    behance: Optional[str] = None
    dribbble: Optional[str] = None
    behance_url: Optional[str] = None
    dribbble_url: Optional[str] = None
    quora_url: Optional[str] = None
    stackoverflow_url: Optional[str] = None
    instagram_url: Optional[str] = None
    youtube_url: Optional[str] = None
    pinterest_url: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    facebook_url: Optional[str] = None
    twitter_url: Optional[str] = None
    website_url: Optional[str] = None
    company_url: Optional[str] = None
    position_url: Optional[str] = None
    address_url: Optional[str] = None
    city_url: Optional[str] = None
    state_url: Optional[str] = None
    zip_url: Optional[str] = None
    country_url: Optional[str] = None
    phone_url: Optional[str] = None
    email_url: Optional[str] = None
    

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "name": "facundo",
    #             "age": "25",
    #             "email": "somebody@gmail.com"
    #         }
    #     }