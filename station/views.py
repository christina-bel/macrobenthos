from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django_tables2 import SingleTableView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .tables import StationTable
from .models import Station

# Create your views here.
def home(request):
    return render(request, 'home.html')

def detail(request, station_id):
    station = get_object_or_404(Station, pk=station_id)
    return render(request, 'station/detail.html', {'station': station})

class StationCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'station.add_station'
    model = Station
    fields = ('descr', 'ddate', 'code', 'num')
    success_url = "/station/list"

class StationListView(PermissionRequiredMixin,SingleTableView):
    permission_required = 'station.view_station'
    model = Station
    paginate_by = 10
    table_class = StationTable
    template_name = 'station/station_list.html'
