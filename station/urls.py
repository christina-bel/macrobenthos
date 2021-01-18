import django.contrib.auth.urls
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
from .views import StationCreateView, StationListView, StationUpdateView, ShipCreateView, ShipListView, ShipUpdateView

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.home, name='home'),
    path('station/<int:station_id>/', views.detail_station, name='detail_station'),
    path('station/new/', StationCreateView.as_view(), name='station_new'),
    path('station/<int:pk>/edit', StationUpdateView.as_view(), name='station_edit'),
    path('station/<int:pk>/delete', views.station_delete, name='station_delete'),
    path('station/list/', StationListView.as_view(), name='station-list'),
    
    path('ship/<int:ship_id>/', views.detail_ship, name='detail_ship'),
    path('ship/new/', ShipCreateView.as_view(), name='ship_new'),
    path('ship/<int:pk>/edit', ShipUpdateView.as_view(), name='ship_edit'),
    path('ship/<int:pk>/delete', views.ship_delete, name='ship_delete'),
    path('ship/list/', ShipListView.as_view(), name='ship-list'),
    
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view())
]
