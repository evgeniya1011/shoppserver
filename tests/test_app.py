import pytest
from passlib.context import CryptContext
from main import app
from tests.conftest import connect_database_test

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Обработчики событий запуска и завершения
def on_startup():
    connect_database_test()


def on_shutdown():
    pass


# Привязка обработчиков событий к приложению
app.add_event_handler("startup", on_startup)
app.add_event_handler("shutdown", on_shutdown)


@pytest.mark.asyncio
async def test_register_user(authenticated_client):
    user_test = {
        "username": "Test Testov",
        "email": "test3@mail.com",
        "phone_number": "+79354571268",
        "password": "Test123$",
        "password_confirmation": "Test123$",

    }
    hashed_password = pwd_context.hash(user_test["password"])
    user_test["password"] = hashed_password
    user_test["password_confirmation"] = hashed_password

    response = authenticated_client.post(
        "/auth/register",
        json=user_test
    )
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_products_unauthorized(client):
    response = client.get("/products/products")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_create_product(client):
    product_test = {
        "name": "Фитнес-браслет",
        "price": 5000
    }
    response = client.post(
        "/products/create-product",
        json=product_test
    )
    assert response.status_code == 200
