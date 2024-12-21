from django.test import TestCase
from .models import Amenity


class AmenitiesModelTest(TestCase):
    """ tests for amenity model. """

    @classmethod
    def setUpTestData(cls):
        """ setting up the data for the tests """
        cls.amenity = Amenity.objects.create(name='Wifi')

    def test_string_representation(self):
        """ test if the model created is correct """
        self.assertEqual(str(self.amenity), 'Wifi')
        self.assertEqual(self.amenity.name, 'Wifi')
