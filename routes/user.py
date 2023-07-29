from fastapi import APIRouter

from models.user import User
from schemas.user import userEntity, userEntityList
from config.db import conn

user = APIRouter()

@user.get("/")
async def find_all_users():
    return userEntityList(conn.bhub.user.find())

@user.post("/")
async def create_user(user: User):
    conn.bhub.user.insert_one(dict(user))
    return userEntityList(conn.bhub.user.find())