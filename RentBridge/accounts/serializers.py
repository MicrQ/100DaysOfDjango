""" Model serializer for the CustomUser model """
from rest_framework import serializers
from django.contrib.auth import authenticate
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


class UserLoginSerializer(serializers.Serializer):
    """ used to serialize the login data """
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        """ used to validate the login data """
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError('Invalid Credentials')
        if not user.is_active:
            raise serializers.ValidationError('User account is deactivated.')

        return user
