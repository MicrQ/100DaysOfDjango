from django.db import models
from rent_bridge.base import Base
from django.contrib.auth import get_user_model


class House(Base):
    """ representation of a rental house """
    owner = models.ForeignKey('accounts.CustomUser',
                              on_delete=models.CASCADE)
    description = models.TextField()
    location = models.ForeignKey('locations.Location',
                                 on_delete=models.CASCADE)
    number_of_room = models.IntegerField(default=1)
    payment_method = models.ForeignKey('payments.PaymentMethod',
                                       on_delete=models.CASCADE,
                                       null=True, blank=True)
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    video = models.FileField(upload_to='house_videos/',
                             blank=True, null=True)


class HouseAmenities(Base):
    """ represents the amenities of a house """
    house = models.ForeignKey('House',
                              on_delete=models.CASCADE)
    amenity = models.ForeignKey('amenities.Amenity',
                                on_delete=models.CASCADE)
