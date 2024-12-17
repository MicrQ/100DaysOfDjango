from django.db import models
from rent_bridge.base import Base
from django.contrib.auth import get_user_model


class House(models.Model, Base):
    """ representation of a rental house """
    owner_id = models.ForeignKey('accounts.CustomUser',
                                 on_delete=models.CASCADE)
    description = models.TextField()
    location = models.ForeignKey('locations.')
    type = models.CharField(max_length=50)
    payment_interval = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    video = models.FileField(upload_to='house_videos/',
                             blank=True, null=True)
