from django.db import models

# Create your models here.
class Entry(models.Model):
    mmsi = models.CharField(max_length=100)
    date = models.DateField(auto_now=False)
    flag = models.CharField(max_length=100)
    eez_crossing = models.CharField(max_length=100)
    violation = models.CharField(max_length=100)



class AIS(models.Model):
    fleet_id = models.IntegerField()
    mmsi = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    lat = models.FloatField()
    lon = models.FloatField()

class FilesAdmin(models.Model):
    upload=models.FileField(upload_to='csvfiles',max_length=150,blank=True)
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title