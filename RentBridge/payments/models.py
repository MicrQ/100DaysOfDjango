from django.db import models
from rent_bridge.base import Base


class PaymentInterval(Base):
    """ representation of the payment interval for a house """
    name = models.CharField(max_length=50)
