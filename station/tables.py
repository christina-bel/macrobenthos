import django_tables2 as tables
from .models import Station, Ship, Species, Family, Genus
from django_tables2.utils import A

class StationTable(tables.Table):
    edit = tables.LinkColumn('station_edit', verbose_name='', text='', args=[A('pk')], orderable=False,
        attrs={'a': {"class": "fa fa-pencil"}})
    delete = tables.LinkColumn('station_delete', verbose_name='', text='', args=[A('pk')], orderable=False,
        attrs={'a': {"class": "fa fa-trash", "onclick": "return confirm('Действительно удалить?')" }})
    class Meta:
        model = Station
        template_name = "django_tables2/bootstrap4.html"
        fields = ('descr', 'ddate', 'code', 'num')
        

class ShipTable(tables.Table):
    edit = tables.LinkColumn('ship_edit', verbose_name='', text='', args=[A('pk')], orderable=False,
        attrs={'a': {"class": "fa fa-pencil"}})
    delete = tables.LinkColumn('ship_delete', verbose_name='', text='', args=[A('pk')], orderable=False,
        attrs={'a': {"class": "fa fa-trash", "onclick": "return confirm('Действительно удалить?')" }})
    class Meta:
        model = Ship
        template_name = "django_tables2/bootstrap4.html"
        fields = ('name', 'eng_name', 'code', 'descr', 'descr_st', 'descr_worm')
        
class SpeciesTable(tables.Table):
    edit = tables.LinkColumn('species_edit', verbose_name='', text='', args=[A('pk')], orderable=False,
        attrs={'a': {"class": "fa fa-pencil"}})
    delete = tables.LinkColumn('species_delete', verbose_name='', text='', args=[A('pk')], orderable=False,
        attrs={'a': {"class": "fa fa-trash", "onclick": "return confirm('Действительно удалить?')" }})
    class Meta:
        model = Species
        template_name = "django_tables2/bootstrap4.html"
        fields = ('name', 'species_name', 'genus_name', 'family', 'author', 'remark')
        
class FamilyTable(tables.Table):
    edit = tables.LinkColumn('family_edit', verbose_name='', text='', args=[A('pk')], orderable=False,
        attrs={'a': {"class": "fa fa-pencil"}})
    delete = tables.LinkColumn('family_delete', verbose_name='', text='', args=[A('pk')], orderable=False,
        attrs={'a': {"class": "fa fa-trash", "onclick": "return confirm('Действительно удалить?')" }})
    class Meta:
        model = Family
        template_name = "django_tables2/bootstrap4.html"
        fields = ('family',)

class GenusTable(tables.Table):
    edit = tables.LinkColumn('genus_edit', verbose_name='', text='', args=[A('pk')], orderable=False,
        attrs={'a': {"class": "fa fa-pencil"}})
    delete = tables.LinkColumn('genus_delete', verbose_name='', text='', args=[A('pk')], orderable=False,
        attrs={'a': {"class": "fa fa-trash", "onclick": "return confirm('Действительно удалить?')" }})
    class Meta:
        model = Genus
        template_name = "django_tables2/bootstrap4.html"
        fields = ('name', 'family_name')
