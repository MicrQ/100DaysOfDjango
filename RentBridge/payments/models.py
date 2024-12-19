from django.db import models
from rent_bridge.base import Base


class PaymentMethod(Base):
    """ representation of the payment methods for a house """
    name = models.CharField(max_length=50)

    def __str__(self):
        """ string representation of the payment method """
        return self.name
