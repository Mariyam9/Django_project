import django_filters

from .models import *


class UniverFilter(django_filters.FilterSet):
    class Meta:
        model = Univer
        fields = ['name']
