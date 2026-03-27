from pydantic import BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber


class UserAddSchemas(BaseModel):
    full_name: str
    phone: PhoneNumber

    model_config = ConfigDict(from_attributes=True)