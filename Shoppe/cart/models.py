from django.db import models
from django.db.models import SET_NULL
from users.models import UserCustomer
from product.models import Product
class Cart(models.Model):
    user = models.ForeignKey(UserCustomer,on_delete=SET_NULL,blank=True,null=True)
    product = models.ForeignKey(Product,on_delete=SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    class Meta:
        db_table='Cart'
class History(models.Model):
    email = models.EmailField(blank=True,null=True)
    phone = models.IntegerField(max_length=10,blank=True,null=True)
    name = models.TextField(blank=True,null=True)
    user = models.ForeignKey(UserCustomer,on_delete=SET_NULL,blank=True,null=True)
    price = models.FloatField(blank=True,null=True)