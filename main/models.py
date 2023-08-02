from django.db import models

class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.IntegerField()
    
    full_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()