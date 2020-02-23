from django.db import models

# Create your models here.
class Customers(models.Model):
    #name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True)
    event = models.TextField()
    leader = models.BooleanField(default=False)
    volunteer = models.BooleanField(default=False)

