import os

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.routers.auth import auth_router
from app.routers.products import product_router
from database import init, close

app = FastAPI()
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')


#запуск
register_tortoise(
    app,
    # db_url="postgres://DB_USERNAME:DB_PASSWORD@localhost:5432/DB_NAME",
    db_url="postgres://postgres:azuhin56@localhost:5432/shop",
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.on_event("startup")
async def startup_db_client():
    await init()


@app.on_event("shutdown")
async def shutdown_db_client():
    await close()


app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(product_router, prefix="/products", tags=["products"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

