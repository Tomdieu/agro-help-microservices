# from django.db import models
from django.contrib.gis.db import models

# Create your models here.


class Soil(models.Model):
    type = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    composition = models.TextField()

    def __str__(self):
        return self.type.capitalize()


class SoilArea(models.Model):
    soil = models.ForeignKey(
        Soil, on_delete=models.CASCADE, related_name='areas')
    polygon = models.PolygonField(srid=4326)

    def __str__(self) -> str:
        return f"{self.soil}"


class Culture(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=1000)
    category = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name.capitalize()

    def image_preview(self):
        return f"<img src='{self.image}' width='300px' height='300px'/>"


class SoilCulture(models.Model):
    id = models.BigIntegerField(primary_key=True)
    soil = models.ForeignKey(
        Soil, on_delete=models.CASCADE, related_name='soil_culture')
    culture = models.ForeignKey(
        Culture, on_delete=models.CASCADE, related_name='soil_culture')

    def __str__(self) -> str:
        return f" {self.soil} culture"

    class Meta:
        unique_together = ('soil', 'culture',)
