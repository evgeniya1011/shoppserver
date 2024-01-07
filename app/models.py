from tortoise import fields, models
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


UserPydantic = pydantic_model_creator(User, name='User')
UserIn_Pydantic = pydantic_model_creator(User, name='UserIn',
                                         exclude_readonly=True)

ProductPydantic = pydantic_model_creator(Product, name='Product')
ProductIn_Pydantic = pydantic_model_creator(Product, name='ProductIn',
                                            exclude_readonly=True)
