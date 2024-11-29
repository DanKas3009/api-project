import requests
from api_project.schema.products import Product
import api_project.config as config

REST_API_URI = config.REST_API_URI

def get_all_products() -> list[Product]:
    response = requests.get(f'{REST_API_URI}/product')
    products = response.json()
    return [Product(**product) for product in products]

def get_product_by_id(product_id: str) -> Product:
    response = requests.get(f'{REST_API_URI}/product/{product_id}')
    product = response.json()
    return Product(**product)

def create_product(product: Product) -> Product:
    response = requests.post(f'{REST_API_URI}/product', json=product.dict())
    return Product(**response.json())