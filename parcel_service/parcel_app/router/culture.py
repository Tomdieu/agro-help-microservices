from fastapi import APIRouter,HTTPException

from typing import List

from .. import schema

from ..models import Culture

router = APIRouter(tags=["Culture"],prefix="/api/culture")



@router.get('/',status_code=200,response_model=List[schema.Culture])
async def list_cultures():
    users = await Culture.all()
    return users


@router.get('/{id}/',response_model=schema.Culture)
async def get_culture(id:int):

    user = await Culture.filter(id=id).first()

    if not user:
        raise HTTPException(status_code=404,detail=f"culture with id={id} not found")
    
    return user
