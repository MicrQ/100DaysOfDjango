from rest_framework import serializers
from .models import House


class HouseSerializer(serializers.ModelSerializer):
    """ serializes the house data and makes validation """
    class Meta:
        model = House
        fields = '__all__'
        