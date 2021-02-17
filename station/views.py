from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView, UpdateView
from django.views.generic.list import ListView
from django_tables2 import SingleTableView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from .tables import StationTable, ShipTable, SpeciesTable, FamilyTable, GenusTable
from .models import Station, Ship, Species, Family, Genus
from .forms import SpeciesForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def detail_station(request, station_id):
    station = get_object_or_404(Station, pk=station_id)
    return render(request, 'station/detail_station.html', {'station': station})

@permission_required('station.delete_station', raise_exception=True)
def station_delete(request, pk):
    Station.objects.filter(id=pk).delete()
    return redirect("/station/list")

class StationCreateView(PermissionRequiredMixin,CreateView):
    permission_required = 'station.add_station'
    model = Station
    fields = ('descr', 'ddate', 'code', 'num')
    template_name = 'station/station_form.html'
    success_url = "/station/list"

class StationUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'station.change_station'
    model = Station
    fields = ('descr', 'ddate', 'code', 'num')
    template_name = 'station/station_form.html'
    success_url = "/station/list"

class StationListView(PermissionRequiredMixin, SingleTableView):
    permission_required = 'station.view_station'
    model = Station
    paginate_by = 10
    ordering = ['ddate', 'num', 'id']
    table_class = StationTable
    template_name = 'station/station_list.html'

@permission_required('station.delete_ship', raise_exception=True)
def ship_delete(request, pk):
    Ship.objects.filter(id=pk).delete()
    return redirect("/ship/list")

class ShipCreateView(PermissionRequiredMixin,CreateView):
    permission_required = 'station.add_ship'
    template_name = 'ship/ship_form.html'
    model = Ship
    fields = ('name', 'eng_name', 'code', 'descr', 'descr_st', 'descr_worm')
    success_url = "/ship/list"

class ShipUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'station.change_ship'
    template_name = 'ship/ship_form.html'
    model = Ship
    fields = ('name', 'eng_name', 'code', 'descr', 'descr_st', 'descr_worm')
    success_url = "/ship/list"

class ShipListView(PermissionRequiredMixin, SingleTableView):
    permission_required = 'station.view_ship'
    model = Ship
    paginate_by = 10
    ordering = ['name', 'id']
    table_class = ShipTable
    template_name = 'ship/ship_list.html'
    
    
@permission_required('station.delete_species', raise_exception=True)
def species_delete(request, pk):
    Species.objects.filter(id=pk).delete()
    return redirect("/species/list")
    
@permission_required('station.load_genus', raise_exception=True)
def load_genus(request):
    family_id = request.GET.get('family')
    genus = Genus.objects.filter(family_name_id=family_id).order_by('name')
    return render(request, 'genus/genus_options.html', {'genus': genus})
    
@permission_required('station.new_item', raise_exception=True)
def new_item(request):
    family = request.GET.get('family')
    genus = request.GET.get('genus')
    isNewFamily = request.GET.get('newFamily')
    nameFamily = Family.objects.create(family=family) if (isNewFamily == 'true') else Family.objects.get(pk=family)
    nameGenus = Genus.objects.create(name=genus, family_name=nameFamily)
    return render(request, 'species/new_item_options.html', {'family': Family.objects.all(), 'selectedFamily': nameFamily.pk, 'genus': Genus.objects.all(), 'selectedGenus': nameGenus.pk})

class SpeciesCreateView(PermissionRequiredMixin,CreateView):
    permission_required = 'station.add_species'
    template_name = 'species/species_form.html'
    model = Species
    form_class = SpeciesForm
    success_url = "/species/list"

class SpeciesUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'station.change_species'
    template_name = 'species/species_form.html'
    model = Species
    form_class = SpeciesForm
    success_url = "/species/list"

class SpeciesListView(PermissionRequiredMixin, SingleTableView):
    permission_required = 'station.view_species'
    model = Species
    paginate_by = 10
    ordering = ['name', 'family', 'id']
    table_class = SpeciesTable
    template_name = 'species/species_list.html'
    
   
@permission_required('station.delete_family', raise_exception=True)
def family_delete(request, pk):
    Family.objects.filter(id=pk).delete()
    return redirect("/family/list")

class FamilyCreateView(PermissionRequiredMixin,CreateView):
    permission_required = 'station.add_family'
    template_name = 'family/family_form.html'
    model = Family
    fields = ('family',)
    success_url = "/family/list"

class FamilyUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'station.change_family'
    template_name = 'family/family_form.html'
    model = Family
    fields = ('family',)
    success_url = "/family/list"

class FamilyListView(PermissionRequiredMixin, SingleTableView):
    permission_required = 'station.view_family'
    model = Family
    paginate_by = 10
    ordering = ['family']
    table_class = FamilyTable
    template_name = 'family/family_list.html'
   

@permission_required('station.delete_genus', raise_exception=True)
def genus_delete(request, pk):
    Genus.objects.filter(id=pk).delete()
    return redirect("/genus/list")

class GenusCreateView(PermissionRequiredMixin,CreateView):
    permission_required = 'station.add_genus'
    template_name = 'genus/genus_form.html'
    model = Genus
    fields = ('name', 'family_name')
    success_url = "/genus/list"

class GenusUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'station.change_genus'
    template_name = 'genus/genus_form.html'
    model = Genus
    fields = ('name', 'family_name')
    success_url = "/genus/list"

class GenusListView(PermissionRequiredMixin, SingleTableView):
    permission_required = 'station.view_genus'
    model = Genus
    paginate_by = 10
    ordering = ['name', 'family_name']
    table_class = GenusTable
    template_name = 'genus/genus_list.html'
