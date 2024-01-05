from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI

import tortoise_config

app = FastAPI()

# async def init():
#     await Tortoise.init(
#         db_url='postgres://postgres:azuhin56@localhost:5432/shop',
#         modules={'models': ['app.models']}
#     )
#     await Tortoise.generate_schemas()
#
#
# async def close():
#     await Tortoise.close_connections()


# def connect_database():
#     register_tortoise(
#         app,
#         # db_url="postgres://DB_USERNAME:DB_PASSWORD@localhost:5432/DB_NAME",
#         config=tortoise_config.TORTOISE_ORM,
#         generate_schemas=True,
#     )


