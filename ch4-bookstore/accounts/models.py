from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """ represents a custom user model.
        instead of using the default user model
    """
    pass