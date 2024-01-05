import os
import sys
import asyncio
import pytest
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import AsyncClient
from tortoise.contrib.fastapi import register_tortoise

from main import connect_database

# app = FastAPI()
#
#
# def initialize_tests():
#     register_tortoise(
#         app,
#         db_url='postgres://postgres:azuhin56@localhost:5432/shop_test',
#         modules={'models': ['app.models']},
#         generate_schemas=True,
#         add_exception_handlers=True,
#     )


# создание TestClient после инициализации Tortoise
# @pytest.fixture
# def client():
#     with TestClient(app) as c:
#         yield c
#
#
# # Фикстура для authenticated_client
# @pytest.fixture
# def authenticated_client():
#     with TestClient(app) as client:
#         yield client

# @pytest.fixture(scope="module")
# def anyio_backend():
#     return "asyncio"
#
#
# @pytest.fixture(scope="module")
# async def client():
#     async with LifespanManager(app):
#         async with AsyncClient(app=app, base_url="http://test") as c:
#             yield c