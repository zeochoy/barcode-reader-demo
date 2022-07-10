from django.db import models

# Create your models here.
class Product(models.Model):
    barcode = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    chi_name = models.CharField(max_length=20, blank=True)
    PRODUCT_TYPE_CHOICES = [('SP', 'Soup'), ('OT', 'Others')]
    type = models.CharField(
        max_length = 2,
        choices = PRODUCT_TYPE_CHOICES,
        default = 'SP',
    )

class Image(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images')
