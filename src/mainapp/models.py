from django.db import models

# Create your models here.

class Location(models.Model):
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)

    def __str__(self):
        return str({0:self.latitude,1:self.longitude})
    

class Profile(models.Model):

    class Status(models.TextChoices):
        rem = "removed"
        tos = "tos"

    id = models.CharField(max_length=30,primary_key=True,on_delete=models.CASCADE)
    loc = models.OneToOneField(Location,max_length=60)
    userId = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=200,blank=True,null=True)
    status = models.CharField(max_length=4,choices=Status,default=Status.rem)
