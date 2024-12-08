""" Model serializer for the CustomUser model """
from rest_framework import serializers
from .models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    """ serializes the user registration data """
    class Meta:
        model = CustomUser
        fields = ['email', 'firstname', 'lastname', 'phone', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """ used to create a new user """
        user = CustomUser.objects.create_user(**validated_data)
        return user
