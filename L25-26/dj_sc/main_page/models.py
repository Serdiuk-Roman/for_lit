from django.db import models

# Create your models here.


class PorterItem(models.Model):
    designer_name = models.CharField(max_length=128)
    link = models.URLField()
    product_name = models.CharField(max_length=128)
    price = models.CharField(max_length=128)
    currency = models.CharField(max_length=128)
    size = models.CharField(max_length=128)
    description = models.TextField()
    images = models.TextField()

    def __str__(self):
        return self.product_name

