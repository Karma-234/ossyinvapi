from fastapi import APIRouter
from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity
from bson import objectid


user = APIRouter()
db = conn.ossyinventory.users

@user.get('/')
async def get_all_users():
    return usersEntity(db.find())


@user.get('/limit=?{amt}')
async def get_limited_users(amt: int):
    return usersEntity(db.find().limit(amt))


@user.get('/{id}')
async def get_single_user(id):
    return userEntity(db.find_one({"id": id}))

@user.post('/')
async def create_user(user: User):
    db.insert_one(dict(user))
    return userEntity(db.find_one({"name": user.name}))

@user.put('/{id}')
async def update_user(id, user: User):
    db.find_one_and_update({"_id": objectid(id)},{"$set":dict(user)})
    return userEntity(db.find_one({"_id": objectid(id)}))

@user.delete('/{id}')
async def delete_user(id, user: User):
    db.find_one_and_delete({"_id": objectid(id)})
    return {"message": "User deleted succesfully"}