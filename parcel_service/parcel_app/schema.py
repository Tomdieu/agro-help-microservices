from . import models

from tortoise.contrib.pydantic.creator import pydantic_model_creator


# UserSchema = pydantic_model_creator(User,name="User",exclude=['id'])
# ParcelSchema = pydantic_model_creator(Parcel,name="Parcel")
# CultureSchema = pydantic_model_creator(Culture,name="Culture")
# CultureParcelSchema = pydantic_model_creator(CultureParcel,name="CultureParcel")


# UserListSchema = pydantic_queryset_creator(User,name="UserList")
# ParcelListSchema = pydantic_queryset_creator(Parcel,name="ParcelList")
# CultureListSchema = pydantic_queryset_creator(Culture)
# CultureListParcelSchema = pydantic_queryset_creator(CultureParcel)

User_Pydantic = pydantic_model_creator(models.User)
UserIn_Pydantic = pydantic_model_creator(models.User, exclude_readonly=True)
Token_Pydantic = pydantic_model_creator(models.Token)
TokenIn_Pydantic = pydantic_model_creator(models.Token, exclude_readonly=True)
Parcel_Pydantic = pydantic_model_creator(models.Parcel, name="ParcelList")
ParcelIn_Pydantic = pydantic_model_creator(models.Parcel, exclude_readonly=True,name="ParcelCreate")
Culture_Pydantic = pydantic_model_creator(models.Culture)
CultureIn_Pydantic = pydantic_model_creator(models.Culture, exclude_readonly=True)
CultureParcel_Pydantic = pydantic_model_creator(models.CultureParcel, exclude=["id"])
CultureParcelIn_Pydantic = pydantic_model_creator(models.CultureParcel, exclude_readonly=True)


from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    type: str


class User(BaseModel):
    id: int
    username: str
    email: str
    type: str

    class Config:
        orm_mode = True


class TokenCreate(BaseModel):
    key: str
    user_id: int


class Token(BaseModel):
    id: int
    key: str
    user: User

    class Config:
        orm_mode = True


class ParcelCreate(BaseModel):
    name: str
    area: float
    user_id: int



class CultureCreate(BaseModel):
    name: str
    image: str
    category: str
    description: str


class Culture(BaseModel):
    id: int
    name: str
    image: str
    category: str
    description: str

    class Config:
        orm_mode = True


class CultureParcelCreate(BaseModel):
    culture_id: int
    parcel_id: int
    longitude: float
    latitude: float




class CultureIds(BaseModel):
    ids:list[int]


class Parcel(BaseModel):
    id: int
    name: str
    area: float
    user: User

    cultures: list[Culture] = []

    class Config:
        orm_mode = True

        

    

class CultureParcel(BaseModel):
    id: int
    culture: Culture
    parcel: Parcel
    longitude: float
    latitude: float

    class Config:
        orm_mode = True