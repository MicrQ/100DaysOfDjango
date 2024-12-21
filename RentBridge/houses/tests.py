from .models import House
from django.test import TestCase
from django.contrib.auth import get_user_model
from locations.models import Location, LocationType


class HousetModelTests(TestCase):
    """ tests for house model. """

    @classmethod
    def setUpTestData(cls):
        """ setting up the data for the tests """
        cls.user = get_user_model().objects.create_user(
            email='test@user.com',
            password='test_password',
            firstname='test',
            lastname='user'
        )
        cls.location_type = LocationType.objects.create(
            name="City"
        )
        cls.location = Location.objects.create(
            name="Hawassa",
            location_type=cls.location_type
        )
        cls.house = House.objects.create(
            owner=cls.user,
            description='A beautiful house',
            location=cls.location,
            number_of_room=3,
            price_per_month=7000.00
        )

    def test_house_model(self):
        """ test if the model is created with correct values """
        self.assertEqual(self.house.owner.email, 'test@user.com')
        self.assertEqual(self.house.owner.firstname, 'test')
        self.assertEqual(self.house.owner.lastname, 'user')
        self.assertEqual(self.house.location.name, 'Hawassa')
        self.assertEqual(self.house.location.location_type.name, 'City')
