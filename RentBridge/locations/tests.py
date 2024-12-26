from django.urls import reverse
from django.test import TestCase
from .models import Location, LocationType
from rest_framework.test import APITestCase


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


class TestLocationTypeAPIView(APITestCase):
    """ tests for location type api view """
    @classmethod
    def setUpTestData(cls):
        pass

    def test_location_type_api_view(self):
        """ test location type api view """
        response = self.client.get(reverse('location_types'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

        response = self.client.post(reverse('location_types'),
                                    {'name': 'Country'})
        self.assertEqual(response.status_code, 401)
        response = self.client.put(reverse('location_types'),
                                   {'name': 'Country'})
        self.assertEqual(response.status_code, 401)
