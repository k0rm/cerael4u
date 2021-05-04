from django.db import models

# Create your models here.

class ProductBrand(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=255, blank=True)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProdImage(models.Model):
    image = models.CharField(max_length=9999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.image

class productNutval(models.Model):
    carbs = models.CharField(max_length=255)