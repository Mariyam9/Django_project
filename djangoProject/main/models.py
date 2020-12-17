from django.db import models
from django.db import connections


class Speciality(models.Model):
    name = models.CharField(max_length=30, blank=True)


class Study(models.Model):
    form = models.CharField(max_length=30, default='full-time')


class Univer(models.Model):
    name = models.CharField(max_length=30, blank=True)
    rating = models.FloatField(max_length=10)
    address = models.CharField(max_length=100, default='Almaty')
    description = models.CharField(max_length=500)
    news = models.CharField(max_length=500, blank=True)
    image = models.ImageField(null=True, blank=True)
    points = models.IntegerField(null=True)
