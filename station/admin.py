from django.contrib import admin

# Register your models here.

from .models import Station, Ship, Species, Family, Genus, Samples


admin.site.register(Samples)
admin.site.register(Station)
admin.site.register(Ship)
admin.site.register(Species)
admin.site.register(Family)
admin.site.register(Genus)
