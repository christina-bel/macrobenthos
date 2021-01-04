from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django_tables2 import SingleTableView
from .tables import StationTable
from .models import Station

# Create your views here.

def detail(request, station_id):
    station = get_object_or_404(Station, pk=station_id)
    return render(request, 'station/detail.html', {'station': station})

class StationCreateView(CreateView):
    model = Station
    fields = ('descr', 'ddate', 'code', 'num')
    success_url = "/station/list"

class StationListView(SingleTableView):
    model = Station
    paginate_by = 10
    table_class = StationTable
    template_name = 'station/station_list.html'
