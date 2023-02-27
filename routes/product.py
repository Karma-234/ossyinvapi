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


@product.get('/limit=?{amt}')
async def get_limited_users(amt: int):
    return productsEntity(db.find().limit(amt))


@product.get('/{id}')
async def get_single_user(id):
    return prodEntity(db.find_one({"id": id}))

@product.post('/')
async def create_user(prod: Product):
    db.insert_one(dict(prod))
    return prodEntity(db.find_one({"name": prod.name}))

@product.put('/{id}')
async def update_user(id, prod: Product):
    db.find_one_and_update({"_id": objectid(id)},{"$set":dict(prod)})
    return prodEntity(db.find_one({"_id": objectid(id)}))

@product.delete('/{id}')
async def delete_user(id, prod: Product):
    db.find_one_and_delete({"_id": objectid(id)})
    return {"message": "User deleted succesfully"}