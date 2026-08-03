from django.db import models
from django.db.models import SET, SET_NULL
from users.models import UserCustomer
class Blog(models.Model):
    title = models.TextField()
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='blog/',blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    author = models.TextField()
    class Meta():
        db_table ='blog'
class Rate(models.Model):
    rate = models.IntegerField(blank=True,null=True)
    blog = models.ForeignKey(Blog,on_delete=SET_NULL,blank=True,null=True)
    user =models.ForeignKey(UserCustomer,on_delete=SET_NULL,blank=True,null=True)
    
