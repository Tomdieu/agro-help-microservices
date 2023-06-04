from fastapi import APIRouter, Depends, HTTPException

from tortoise.contrib.fastapi import HTTPNotFoundError


from typing import List

from ..models import Parcel, Culture, CultureParcel

from .. import schema
from ..models import User
from ..middleware.authenticate_token import authenticate_token

router = APIRouter(prefix="/api/parcel", tags=["Parcel"])
schema.Culture_Pydantic

async def convert_to_pydantic(parcel):
    parcel_data = await schema.ParcelPydantic.from_tortoise_orm(parcel)
    cultures_data = await schema.CulturePydantic.from_queryset(parcel.cultures.all())
    parcel_data.cultures = cultures_data
    return parcel_data


@router.get("/", status_code=200, response_model=List[schema.Parcel])
async def list_parcels(user: User = Depends(authenticate_token)):
    parcels = await Parcel.filter(user=user).all().prefetch_related("cultures")
    print("Parcels", parcels)
    return [convert_to_pydantic(parcel) for parcel in parcels]
    # return await ParcelListSchema.from_queryset(parcels)


@router.get(
    "/{id}/",
    status_code=200,
    response_model=schema.Parcel,
    responses={404: {"model": HTTPNotFoundError}},
)
async def get_parcel(id: int, user: User = Depends(authenticate_token)):
    parcel = await Parcel.filter(id=id).first()
    if not parcel:
        raise HTTPException(
            status_code=404, detail="parcel with id={id} not found".format(id=id)
        )
    return convert_to_pydantic(parcel)


# @router.post('',response_model=schema.Parcel)
@router.post("/", response_model=schema.Parcel, status_code=201)
async def create_parcel(
    parcel: schema.ParcelIn_Pydantic, user: User = Depends(authenticate_token)
):
    new_parcel = await Parcel.create(user=user, **parcel.dict(exclude_unset=True))
    return new_parcel
    # return await schema.Parcel.from_tortoise_orm(new_parcel)


@router.patch("/{id}/", response_model=schema.Parcel)
# @router.patch('/{id}',response_model=schema.Parcel)
async def update_parcel(
    id: int, parcel: schema.ParcelIn_Pydantic, user: User = Depends(authenticate_token)
):
    
    await Parcel.filter(id=id, user=user).update(**parcel.dict(exclude_unset=True))
    updated_parcel_obj = await Parcel.filter(id=id, user=user).first()
    if not update_parcel:
        raise HTTPException(status_code=404, detail="Parcel not found")
    return updated_parcel_obj
    # return await schema.Parcel.from_tortoise_orm(updated_parcel_obj)


@router.put("/{id}/", response_model=schema.Parcel)
# @router.put('/{id}',response_model=schema.Parcel)
async def update_parcel(
    id: int, parcel: schema.ParcelIn_Pydantic, user: User = Depends(authenticate_token)
):
    await Parcel.filter(id=id, user=user).update(**parcel.dict(exclude_unset=True))
    updated_parcel_obj = await Parcel.filter(id=id, user=user).first()
    if not update_parcel:
        raise HTTPException(status_code=404, detail="Parcel not found")
    return updated_parcel_obj
    # return await schema.Parcel.from_tortoise_orm(updated_parcel_obj)


# @router.delete("/{id}", response_model=dict)
@router.delete("/{id}/", response_model=dict)
async def delete_parcel(id: int, user: User = Depends(authenticate_token)):
    deleted_count = await Parcel.filter(id=id, user=user).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail="Parcel not found")
    return {"message": "Parcel deleted successfully"}


@router.post(
    "/{id}/add_cultures",
    response_model=dict,
    summary="This route add a list of cultures to a parcel",
)
async def add_cultures(id: int, cultureIds: schema.CultureIds):
    parcel = await Parcel.filter(id=id).first()
    cultures_added = []
    for culture_id in cultureIds.ids:
        culture = await Culture.filter(id=culture_id).first()

        if culture:
            await CultureParcel.create(culture=culture, parcel=parcel)
            cultures_added.append(culture)

    return {
        "message": f"{len(cultures_added)} cultures added to you parcel successfully"
    }


@router.post(
    "/{id}/suggest_culture/",
    response_model=dict,
    summary="This route suggest a list of culture for a parcel",
    status_code=200,
)
async def suggest_culture(id: int):
    # here we are going to make a request to the soil service to get the favorable crops of a parcel
    return {"message": "Not yet available"}
