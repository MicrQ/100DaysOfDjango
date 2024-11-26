from django.db import models


class Book(models.Model):
    """ book representation """

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        """ string representation of the model """
        return self.title
