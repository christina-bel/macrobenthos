from django.contrib import admin

# Register your models here.

from .models import Station, Ship

admin.site.register(Station)
admin.site.register(Ship)
