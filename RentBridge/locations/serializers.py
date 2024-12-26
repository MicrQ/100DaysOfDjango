from rest_framework import serializers
from .models import Location, LocationType


class LocationTypeSerializer(serializers.ModelSerializer):
    """ serializes the location type model's data and makes validation """
    class Meta:
        model = LocationType
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    """ serializes the location model's data and makes validation """
    class Meta:
        model = Location
        fields = '__all__'
