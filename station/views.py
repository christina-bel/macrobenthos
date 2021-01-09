from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView, UpdateView
from django.views.generic.list import ListView
from django_tables2 import SingleTableView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from .tables import StationTable
from .models import Station

# Create your views here.
def home(request):
    return render(request, 'home.html')

def detail(request, station_id):
    station = get_object_or_404(Station, pk=station_id)
    return render(request, 'station/detail.html', {'station': station})

@permission_required('station.delete_station', raise_exception=True)
def station_delete(request, pk):
    Station.objects.filter(id=pk).delete()
    return redirect("/station/list")

class StationCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'station.add_station'
    model = Station
    fields = ('descr', 'ddate', 'code', 'num')
    success_url = "/station/list"

class StationUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'station.change_station'
    model = Station
    fields = ('descr', 'ddate', 'code', 'num')
    success_url = "/station/list"

class StationListView(PermissionRequiredMixin,SingleTableView):
    permission_required = 'station.view_station'
    model = Station
    paginate_by = 10
    ordering = ['ddate', 'num', 'id']
    table_class = StationTable
    template_name = 'station/station_list.html'
