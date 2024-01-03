from tortoise import Tortoise


async def init():
    await Tortoise.init(
        db_url='postgres://postgres:azuhin56@localhost:5432/shop',
        modules={'models': ['app.models']}
    )
    await Tortoise.generate_schemas()


async def close():
    await Tortoise.close_connections()


