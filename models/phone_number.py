from ast import Dict
import re
from typing import Any
from pydantic.validators import str_validator

class PhoneNumber(str):
    """Phone number type"""

    @classmethod
    def __get_validators__(cls) -> Dict[str, Any]:
        yield str_validator
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(
            pattern=r'^\+?[0-9]+$',
            example=['+541112345678'],
            format='phone-number',
        )

    @classmethod
    def validate(cls, value: str) -> str:
        PHONE_REGEXP = re.compile(r'^\+?[0-9]{1,3}?[0-9]{6,14}$')
        if not isinstance(value, str):
            raise TypeError('Phone number must be a string')

        match = PHONE_REGEXP.search(value)

        if not match:
            raise ValueError('Phone number must be a valid phone number')

        return value

    def __repr__(self) -> str:
        return f'PhoneNumber({super().__repr__()})'