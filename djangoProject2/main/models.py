from django.db import models


class Point(models.Model):
    point = models.FloatField(primary_key=True, max_length=30, default=0)
    pass


class Speciality(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    points = models.ManyToManyField(Point)
    pass


class Study(models.Model):
    form = models.CharField(max_length=30, primary_key=True)
    pass


class Univer(models.Model):
    name = models.CharField(max_length=30, blank=True, primary_key=True)
    rating = models.FloatField(max_length=10, default=0)
    address = models.CharField(max_length=100, default='Almaty')
    description = models.CharField(max_length=500)
    news = models.CharField(max_length=500, blank=True)
    image = models.ImageField(null=True, blank=True)
    specialities = models.ManyToManyField(Speciality, default='default')
    form_of_study = models.ManyToManyField(Study, default='full-time')



class Abiturient(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)


