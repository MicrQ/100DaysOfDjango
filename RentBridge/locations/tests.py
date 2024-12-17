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


class LocationModelTests(TestCase):
    """ tests for location model """
    @classmethod
    def setUpTestData(cls):
        cls.location_type = LocationType.objects.create(
            name="Country"
        )
        cls.location = Location.objects.create(
            name="Kenya",
            location_type=cls.location_type
        )

    def test_location_name(self):
        """ test location name """
        self.assertEqual(self.location.name, "Kenya")

    def test_location_type(self):
        """ test location type """
        self.assertEqual(self.location.location_type.name, "Country")

    def test_location_str(self):
        """ test string representation of location """
        self.assertEqual(str(self.location), "Kenya")

    def test_location_parent(self):
        """ test location parent """
        parent_location = Location.objects.create(
            name="Africa",
            location_type=self.location_type
        )
        self.location.parent = parent_location
        self.location.save()
        self.assertEqual(self.location.parent.name, "Africa")
