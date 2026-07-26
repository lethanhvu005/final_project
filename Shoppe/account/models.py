from django.db import models
from django.contrib.auth.models import AbstractUser
class Country(models.Model):
    name = models.CharField(max_length=255, blank=True,null=True)
class UserCustomer(AbstractUser):
    avatar = models.ImageField(upload_to='account/', blank=True,null=True)
    confirm_password = models.CharField(max_length=255,blank=True,null=True)
    id_country = models.ForeignKey(Country,on_delete=models.SET_NULL,blank=True,null=True)
    