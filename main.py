from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

import tortoise_config
from app.routers.auth import auth_router
from app.routers.products import product_router

app = FastAPI()


def connect_database():
    register_tortoise(
        app,
        config=tortoise_config.TORTOISE_ORM,
        generate_schemas=True,
    )


app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(product_router, prefix="/products", tags=["products"])

if __name__ == "__main__":
    import uvicorn
    connect_database()
    uvicorn.run(app, host="127.0.0.1", port=8000)
