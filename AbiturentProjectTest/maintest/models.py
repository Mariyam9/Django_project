from django.db import models
from django.db import connections


def CASCADE(collector, field, sub_objs, using):
    collector.collect(sub_objs, source=field.remote_field.model,
                      source_attr=field.name, nullable=field.null)
    if field.null and not connections[using].features.can_defer_constraint_checks:
        collector.add_field_update(field, None, sub_objs)


class Speciality(models.Model):
    name = models.CharField(max_length=30, blank=True)
    pass


class Study(models.Model):
    form = models.CharField(max_length=30, default='full-time')
    pass


class Univer(models.Model):
    name = models.CharField(max_length=30, blank=True)
    rating = models.FloatField(max_length=10, default=0)
    address = models.CharField(max_length=100, default='Almaty')
    description = models.CharField(max_length=500)
    news = models.CharField(max_length=500, blank=True)
    image = models.ImageField(null=True, blank=True)
    specialities = models.ForeignKey(Speciality, on_delete=models.CASCADE, default='default')
    points = models.IntegerField(null=True)
    form_of_study = models.ForeignKey(Study, on_delete=models.CASCADE, default='full-time')


