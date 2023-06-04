from tortoise import models, fields


class User(models.Model):
    id = fields.IntField(pk=True, generated=False)
    username = fields.CharField(120, unique=True)
    email = fields.CharField(255)
    type = fields.CharField(50)
    is_staff = fields.BooleanField(default=False)
    is_superuser = fields.BooleanField(default=False)

    class Meta:
        table = "users"


class Token(models.Model):
    id = fields.IntField(pk=True)
    key = fields.CharField(255)
    user: fields.ForeignKeyRelation[User] = fields.OneToOneField(
        "models.User", related_name="token"
    )

    class Meta:
        table = "tokens"


class Parcel(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(255)
    area = fields.FloatField(description="size in square meters")

    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User", related_name="parcels"
    )
    longitude = fields.FloatField(null=False)
    latitude = fields.FloatField(null=False)
    cultures: fields.ReverseRelation["CultureParcel"]

    class Meta:
        table = "parcels"


class Culture(models.Model):
    id = fields.IntField(pk=True, generated=False)
    name = fields.CharField(255)
    image = fields.CharField(255)
    category = fields.CharField(255)
    description = fields.TextField()

    class Meta:
        table = "cultures"


class CultureParcel(models.Model):
    id = fields.IntField(pk=True)
    culture: fields.ForeignKeyRelation[Culture] = fields.ForeignKeyField(
        "models.Culture", related_name="parcels"
    )
    parcel: fields.ForeignKeyRelation[Parcel] = fields.ForeignKeyField(
        "models.Parcel", related_name="cultures"
    )

    class Meta:
        table = "culture_parcel"
