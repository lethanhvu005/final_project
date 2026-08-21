from sre_constants import BRANCH
from django.db import models
from django.db.models import SET_NULL
from users.models import UserCustomer
class Category(models.Model):
    name = models.TextField(blank=True, null=True)
    class Meta():
        db_table ='Category'
    def __str__(self):
        return self.name
class Brand(models.Model):
    name = models.TextField(blank=True, null=True)
    class Meta():
        db_table ='Brand'
    def __str__(self):
        return self.name
class Product(models.Model):
    user=models.ForeignKey(UserCustomer,on_delete=SET_NULL,blank=True, null=True)
    name = models.TextField(max_length=50,blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    image =models.JSONField(default=list,blank=True, null=True)
    sale = models.IntegerField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=SET_NULL,blank=True, null=True)
    brand = models.ForeignKey(Brand ,on_delete=SET_NULL,blank=True, null=True)
    status = models.IntegerField(default=0,blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    STATUS =[('sale','Sale'),
             ('normal','Normal')]
    status =models.TextField(max_length=20,choices=STATUS,blank=True,null=True)
    class Meta():
        db_table = 'Product'
