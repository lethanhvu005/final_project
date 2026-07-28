from django.contrib.auth.models import AbstractUser 
from django.db import models
from country.models import Country
class UserCustomer(AbstractUser):
    avatar = models.ImageField(upload_to='users/',blank=True , null=True)
    id_country = models.ForeignKey(Country,on_delete=models.SET_NULL, blank=True , null= True)
    
    

