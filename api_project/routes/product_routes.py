from fastapi import APIRouter, HTTPException
from api_project.schema.products import Product

from api_project.service import products_services

router = APIRouter()

@router.get('/products', response_model=list[Product])
async def get_all_products():
    return products_services.get_all_products()

@router.get('/products/{product_id}', response_model=Product)
async def get_product_by_id(product_id: str):
    product = products_services.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    return product

@router.post('/products', response_model=Product)
async def create_product(product: Product):
    return products_services.create_product(product)

# uvicorn api_project.main:app --reload