from django.db import models

# Create your models here.

"""services model"""



"""teams model"""



"""portfolio model"""



"""analytics model"""
class Analytic(models.Model):
    client = models.IntegerField()
    projects = models.IntegerField()
    hoursOfSupport = models.IntegerField()
    workers = models.IntegerField()


    # """defining a name for each entry"""
    # def __str__(self):
    #     return "analytics"

