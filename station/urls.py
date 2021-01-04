from django.urls import path

from . import views
from .views import StationCreateView, StationListView

urlpatterns = [
    path('', StationListView.as_view(), name='station-list'),
    path('<int:station_id>/', views.detail, name='detail'),
    path('station/new/', StationCreateView.as_view(), name='station_new'),
    path('station/list/', StationListView.as_view(), name='station-list')
]
