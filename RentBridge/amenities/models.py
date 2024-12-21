from django.db import models
from rent_bridge.base import Base


class Amenity(Base):
    """ a representation of an amenity of a house """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
