import django_tables2 as tables
from .models import Station

class StationTable(tables.Table):
    class Meta:
        model = Station
        template_name = "django_tables2/bootstrap.html"
        fields = ('descr', 'ddate', 'code', 'num')
