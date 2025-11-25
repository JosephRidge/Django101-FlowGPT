from django.db import models

# Create your models here.
class Bottle(models.Model):
    name = models.CharField(max_length=200)
    size = models.FloatField()
    color = models.CharField(max_length=100)
    price = models.FloatField()
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Name: {self.name} || Color: {self.color} "