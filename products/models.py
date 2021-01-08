from django.db import models


class Product(models.Model):
    sku = models.CharField(max_length=1000, unique=True)
    name = models.CharField(max_length=255, blank=True, default='')
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['name']
