from django.test import TestCase
from .models import Location, LocationType


class LocationTypeTests(TestCase):
    """ tests to check if locationtype model """
    @classmethod
    def setUpTestData(cls):
        cls.location_type = LocationType.objects.create(
            name="Country"
        )

    def test_location_type(self):
        """ test location_type model """
        self.assertEqual(self.location_type.name, "Country")
        self.assertEqual(str(self.location_type), "Country")
