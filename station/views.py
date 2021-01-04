from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView
from django.views.generic.list import ListView

from .models import Station
# Create your views here.

def detail(request, station_id):
    station = get_object_or_404(Station, pk=station_id)
    return render(request, 'station/detail.html', {'station': station})

class StationCreateView(CreateView):
    model = Station
    fields = ('descr', 'ddate', 'code', 'num')
    success_url = "/station/list"

class StationListView(ListView):
    model = Station
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context
