from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class Bucket(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True , blank=True)

class ProductBucket(models.Model):
    count = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # я немного не понял на счет бакета, мы изначально указали связь фор ин кей, но на какой класс он ориентируеться ? тут я немножко не понял


    # bucket = models.ForeignKey()

