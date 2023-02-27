from fastapi import APIRouter
from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity


user = APIRouter()

@user.get('/users/')
async def get_all_users():
    return usersEntity(conn.ossyinventory.users.find())


@user.get('/users/limit=?{amt}')
async def get_limited_users(amt: int):
    return usersEntity(conn.ossyinventory.users.find().limit(amt))


@user.get('/user/{id}')
async def get_single_user(id):
    return userEntity(conn.ossyinventory.users.find_one({"id": id}))