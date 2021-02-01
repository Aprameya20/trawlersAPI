from django.db import models

# Create your models here.
class Entry(models.Model):
    mmsi = models.CharField(max_length=100)
    date = models.DateField(auto_now=False)
    flag = models.CharField(max_length=100)
    eez_crossing = models.CharField(max_length=100)
    violation = models.CharField(max_length=100)