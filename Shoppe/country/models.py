from django.db import models
class Country(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name