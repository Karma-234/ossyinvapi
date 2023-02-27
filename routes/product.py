from fastapi import APIRouter
from models.product import Product
from config.db import conn
from schemas.product import prodEntity, productsEntity
from bson import objectid

product = APIRouter()
db = conn.ossyinventory.products

@product.get('/products/')
async def get_all_products():
    return productsEntity(db.find())