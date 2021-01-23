from django.contrib import admin

# Register your models here.

from .models import Station, Ship, Species

admin.site.register(Station)
admin.site.register(Ship)
admin.site.register(Species)
