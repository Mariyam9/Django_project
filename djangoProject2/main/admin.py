from django.contrib import admin
from .models import *


class AbiturientAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'username', 'password', 'email', 'country', 'city']


admin.site.register(Point)
admin.site.register(Speciality)
admin.site.register(Study)
admin.site.register(Univer)
admin.site.register(Abiturient, AbiturientAdmin)



