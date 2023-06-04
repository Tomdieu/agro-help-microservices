from fastapi import APIRouter, HTTPException

from typing import List

from .. import schema

from ..models import User, Token

router = APIRouter(tags=["User"], prefix="/api/user")


@router.get("/", status_code=200, response_model=List[schema.User])
async def list_users():
    users = await User.all()
    for user in users:
        token = await Token.filter(user=user).first()
        print(token.key)
    return users


@router.get("/{id}/", response_model=schema.User)
async def get_user(id: int):
    user = await User.filter(id=id).first()

    if not user:
        raise HTTPException(status_code=404, detail=f"user with id={id} not found")

    return user
