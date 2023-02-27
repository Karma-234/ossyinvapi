from fastapi import APIRouter
from models.product import Product
from config.db import conn
from schemas.product import prodEntity, productsEntity


product = APIRouter()

@product.get('/products/')
async def get_all_products():
    return productsEntity(conn.ossyinventory.products.find())