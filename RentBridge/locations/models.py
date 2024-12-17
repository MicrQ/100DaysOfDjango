from django.db import models
from rent_bridge.base import Base



class Location(models.Model, Base):
    """ represents location(Country, Region, City) """
    pass


class LocationType(models.Model, Base):
    """ represents location type
        MUST BE POPULATED MANUALLY or with SEEDER
    """
    name = models.CharField(max_length=50)
