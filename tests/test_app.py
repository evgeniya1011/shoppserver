import asyncio

import anyio
import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient
from tortoise import Tortoise

from app.models import User
from main import connect_database, app

ANYIO_FORCE_BACKEND = asyncio
async def init_db():
    # инициализация базы данных перед тестами
    await Tortoise.init(
        db_url='postgres://postgres:azuhin56@localhost:5432/shop_test',
        modules={"models": ["app.models"]},
    )
    await Tortoise.generate_schemas()


async def cleanup_db():
    # очистка базы данных после тестов
    await Tortoise.close_connections()


@pytest.fixture(autouse=True)
async def setup_and_teardown():
    await init_db()
    yield
    await cleanup_db()


@pytest.mark.anyio
async def test_register_user():
    user_test = {
            "username": "Test Testov",
            "email": "test@example.com",
            "phone_number": "+71234567890",
            "password": "Test123$",
            "password_confirmation": "Test123$",

        }
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Отправка запроса на регистрацию
        response = await client.post("/auth/register", json=user_test)

        # Проверка успешного ответа и наличия созданного пользователя в базе данных
        assert response.status_code == 200
        assert response.json()["username"] == user_test["username"]

        # # Проверка, что пароль сохранен в хешированном виде
        user_id = response.json()["id"]
        registered_user = await User.get(id=user_id)
        assert registered_user.id == user_id
        # Очистка данных после теста
        await User.filter(id=user_id).delete()
    await cleanup_db()

#
# @pytest.fixture(autouse=True)
# async def setup_and_teardown():
#     await init_db()
#     yield
#     await cleanup_db()


# async def main():
#     await init_db()
#     await test_register_user()
#     await cleanup_db()
#
# anyio.run(main)

# @pytest.mark.anyio
# async def test_create_user(client: AsyncClient):  # nosec
#     response = await client.post("/users", json={"username": "admin"})
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data["username"] == "admin"
#     assert "id" in data
#     user_id = data["id"]
#
#     user_obj = await Users.get(id=user_id)
#     assert user_obj.id == user_id