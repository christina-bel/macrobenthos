import django_tables2 as tables
from .models import Station, Ship
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
        

class ShipTable(tables.Table):
    edit = tables.LinkColumn('ship_edit', verbose_name='', text='', args=[A('pk')], orderable=False,
        attrs={'a': {"class": "fa fa-pencil"}})
    delete = tables.LinkColumn('ship_delete', verbose_name='', text='', args=[A('pk')], orderable=False,
        attrs={'a': {"class": "fa fa-trash", "onclick": "return confirm('Действительно удалить?')" }})
    class Meta:
        model = Ship
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'eng_name', 'code', 'descr', 'descr_st', 'descr_worm')
