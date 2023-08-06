from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    diagonal = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    image = models.ImageField()
    category  = models.ManyToManyField(Category)