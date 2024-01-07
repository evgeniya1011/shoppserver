import pytest
from fastapi.testclient import TestClient
from tortoise.contrib.fastapi import register_tortoise

import tortoise_config
from main import app


def connect_database_test():
    register_tortoise(
        app,
        # db_url="postgres://DB_USERNAME:DB_PASSWORD@localhost:5432/DB_NAME",
        config=tortoise_config.TORTOISE_ORM_TEST,
        generate_schemas=True,
    )


# Фикстура создания TestClient после инициализации Tortoise
@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


# Фикстура для authenticated_client
@pytest.fixture
def authenticated_client():
    with TestClient(app) as client:
        yield client
