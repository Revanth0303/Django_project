from django.db import models

# Create your models here.
class Offers(models.Model):
    
    name=models.CharField(max_length=200)
    timings=models.CharField(max_length=200)
    discount=models.CharField(max_length=200)
    offer=models.BooleanField(default=False)