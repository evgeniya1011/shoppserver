from pydantic import BaseModel, EmailStr, field_validator, model_validator
import re


class UserRegistration(BaseModel):
    username: str
    email: EmailStr
    phone_number: str
    password: str
    password_confirmation: str

    @field_validator('phone_number')
    def validate_phone_number(cls, value):
        if not re.match(r'^\+7\d{10}$', value):
            raise ValueError('Неверный формат номера телефона')
        return value

    @field_validator('password')
    def validate_password(cls, value):
        if (len(value) < 8 or not any(char.isupper() for char in value) or
                not any(char in '$%&!:' for char in value)):
            raise ValueError('Неверный формат пароля')
        return value

    @model_validator(mode='before')
    def validate_password_confirmation(cls, values):
        password = values.get('password')
        password_confirmation = values.get('password_confirmation')
        if password != password_confirmation:
            raise ValueError('Пароли не совпадают')
        return values


class UserLogin(BaseModel):
    email_phone_number: str
    password: str


class ProductCreate(BaseModel):
    name: str
    price: int
