from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Soil, SoilArea, SoilCulture
from rest_framework import serializers as sz
from rest_framework_gis import serializers


class _SoilSerializer(sz.ModelSerializer):
    class Meta:
        model = Soil
        fields = "__all__"


class SoilSerializer(sz.ModelSerializer):
    composition = sz.SerializerMethodField()

    class Meta:
        model = Soil
        fields = "__all__"

    def get_composition(self, soil: Soil):
        return soil.composition.split("|")


class SoilSerializerCreate(sz.ModelSerializer):

    class Meta:
        model = Soil
        fields = "__all__"

    def get_composition(self, soil: Soil):
        return soil.composition.split("|")

class SoilAreaSerializer(serializers.GeoFeatureModelSerializer):
    soil = SoilSerializer()

    class Meta:
        model = SoilArea
        geo_field = "polygon"
        fields = ("soil", "polygon")
        
class SoilAreaSerializerCreate(serializers.GeoFeatureModelSerializer):

    class Meta:
        model = SoilArea
        geo_field = "polygon"
        fields = ("soil","polygon")
