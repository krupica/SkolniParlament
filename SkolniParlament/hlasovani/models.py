from django.db import models

# Create your models here.
class Student(models.Model):
    jmeno = models.CharField(max_length=30)
    prijmeni = models.CharField(max_length=30)
    trida = models.CharField(max_length=10)
    email = models.CharField(max_length=70)
    token = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)
    voted = models.BooleanField