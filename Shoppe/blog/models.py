from django.db import models
class Blog(models.Model):
    title = models.TextField()
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='blog/',blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    author = models.TextField()
    class Meta():
        db_table ='blog'