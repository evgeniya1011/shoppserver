from pydantic import BaseModel, EmailStr, field_validator
from tortoise import fields, models
import re

from tortoise.contrib.pydantic import pydantic_model_creator


class User(models.Model):
    """Модель пользователя"""

    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, null=True)
    email = fields.CharField(max_length=50, unique=True)
    phone_number = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=128, null=True)
    password_confirmation = fields.CharField(max_length=128, null=True)

    def __str__(self):
        return f'{self.username}'

    class PydanticMeta:
        exclude = ['password']

    def __get_pydantic_model__(self):
        return UserPydantic


# class UserRegistration(BaseModel):
#     username: str
#     email: EmailStr
#     phone_number: str
#     password: str
#     password_confirmation: str
#
#     @field_validator('phone_number')
#     def validate_phone_number(cls, value):
#         if not re.match(r'^\+7\d{10}$', value):
#             raise ValueError('Неверный формат номера телефона')
#         return value
#
#     @field_validator('password')
#     def validate_password(cls, value):
#         if len(value) < 8 or not any(char.isupper() for char in value) or not any(char in '$%&!:' for char in value):
#             raise ValueError('Неверный формат пароля')
#         return value
#
#     @field_validator('password_confirmation')
#     def validate_password_confirmation(cls, value, **values):
#         print(values)
#         if "password" in values and value != values["password"]:
#             raise ValueError("Пароли не совпадают")
#         return value
#
#
# class UserLogin(BaseModel):
#     email_phone_number: str
#     password: str



class Product(models.Model):
    """Модель товара"""

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    price = fields.IntField(pk=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    is_active = fields.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.price}'


    def __get_pydantic_model__(self):
        return ProductPydantic


# class ProductCreate(BaseModel):
#     name: str
#     price: int


UserPydantic = pydantic_model_creator(User, name='User')
UserIn_Pydantic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)

ProductPydantic = pydantic_model_creator(Product, name='Product')
ProductIn_Pydantic = pydantic_model_creator(Product, name='ProductIn', exclude_readonly=True)



