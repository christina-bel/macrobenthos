import django_tables2 as tables
from .models import Station
from django_tables2.utils import A

class StationTable(tables.Table):
    edit = tables.LinkColumn('station_edit', verbose_name='', text='', args=[A('pk')], orderable=False,
        attrs={'a': {"class": "fa fa-pencil"}})
    delete = tables.LinkColumn('station_delete', verbose_name='', text='', args=[A('pk')], orderable=False,
        attrs={'a': {"class": "fa fa-trash", "onclick": "return confirm('Действительно удалить?')" }})
    class Meta:
        model = Station
        template_name = "django_tables2/bootstrap.html"
        fields = ('descr', 'ddate', 'code', 'num')
