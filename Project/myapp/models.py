from tokenize import Name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Feature(models.Model):
    head = models.CharField(max_length= 100)
    details = models.CharField(max_length= 500)
    link = models.CharField(max_length=700)
   

class Blog(models.Model):
    head =  models.CharField(max_length= 1000)
    body =  models.CharField(max_length= 10000)

