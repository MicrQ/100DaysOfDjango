""" Contains the CustomUserManager and CustomUser models """
from django.db import models
from rent_bridge.base import Base
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class CustomUserManager(BaseUserManager):
    """ used to customize the user model and its methods """

    def create_user(self, email, firstname, lastname,
                    password=None, **extra_fields):
        """ used to override the default create_user method """
        if not email:
            raise ValueError('The Email field must be set')
        if not firstname:
            raise ValueError('The Firstname field must be set')
        if not lastname:
            raise ValueError('The Lastname field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, firstname=firstname,
                          lastname=lastname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, firstname, lastname,
                         password=None, **extra_fields):
        """ used to override the default superuser creation method """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, firstname, lastname,
                                password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin, Base):
    """ Custom user model: used to add more attributes """
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, unique=True,
                             blank=True, null=True)
    profile_image = models.ImageField(
        upload_to='profile_images/', blank=True, null=True)
    id_image = models.ImageField(upload_to='id_images/',
                                 blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    def __str__(self):
        return self.email
