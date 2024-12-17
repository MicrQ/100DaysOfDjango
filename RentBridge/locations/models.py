from django.db import models
from rent_bridge.base import Base



class Location(Base):
    """ represents location(Country, Region, City) """
    pass


class LocationType(Base):
    """ represents location type
        MUST BE POPULATED MANUALLY or with SEEDER
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        """ string representation of location type """
        return self.name
