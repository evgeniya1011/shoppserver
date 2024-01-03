from fastapi import APIRouter, Depends
from app.models import Product, ProductPydantic
from app.schemas import ProductCreate
from app.utils import get_current_user

product_router = APIRouter()


@product_router.get("/products", response_model=list[ProductPydantic])
async def get_products(page: int = 1, page_size: int = 10, current_user=Depends(get_current_user)):
    products = await Product.filter(is_active=True).offset(page).limit(page_size).all()
    return products


@product_router.post("/create-product", response_model=ProductPydantic)
async def create_product(product: ProductCreate):
    new_product = await Product.create(name=product.name, price=product.price)
    return await ProductPydantic.from_tortoise_orm(new_product)


