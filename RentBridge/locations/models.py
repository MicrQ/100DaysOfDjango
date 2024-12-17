from django.db import models
from rent_bridge.base import Base


class Location(Base):
    """ represents location(Country, Region, City) """
    name = models.CharField(max_length=50, unique=True)
    location_type = models.ForeignKey('LocationType',
                                      on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               blank=True, null=True)

    def __str__(self):
        """ string representation of location """
        return self.name


class LocationType(Base):
    """ represents location type
        MUST BE POPULATED MANUALLY or with SEEDER
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        """ string representation of location type """
        return self.name
