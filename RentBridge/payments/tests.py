from django.test import TestCase
from .models import PaymentMethod


class PaymentMethodTestCase(TestCase):
    """ test cases for the PaymentMethod model """
    @classmethod
    def setUpTestData(cls):
        """ setting up the test data """
        cls.payment_method = PaymentMethod.objects.create(name="CASH")

    def test_payment_model_creation(self):
        """ test the name of the payment interval """
        self.assertEqual(self.payment_method.name, "CASH")
        self.assertEqual(str(self.payment_method), "CASH")
