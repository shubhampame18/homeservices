from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class CustomerUser(models.Model):
    username = models.CharField(max_length=10)
    pwd = models.CharField(max_length=10)
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    contact = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    address = models.TextField(max_length=50)
    city = models.CharField(max_length=10)
    image = models.FileField()
    usertype = models.CharField(max_length=15)

    def __str__(self):
        return self.email
