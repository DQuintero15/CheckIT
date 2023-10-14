from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class BaseBusinessLocation(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

class BaseBusinessInfo(BaseBusinessLocation):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    slogan = models.CharField(max_length=100)
    

class Enterprise(BaseBusinessInfo):
    nit = models.CharField(max_length=16)
    pass


class IndependentTechnician(BaseBusinessInfo):
    document = models.CharField(max_length=16)
    pass


class Client(BaseBusinessLocation):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    pass
