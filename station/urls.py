import django.contrib.auth.urls
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
from .views import StationCreateView, StationListView, StationUpdateView, ShipCreateView, ShipListView, ShipUpdateView, SpeciesCreateView, SpeciesListView, SpeciesUpdateView, FamilyCreateView, FamilyListView, FamilyUpdateView, GenusCreateView, GenusListView, GenusUpdateView

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.home, name='home'),
    path('station/<int:station_id>/', views.detail_station, name='detail_station'),
    path('station/new/', StationCreateView.as_view(), name='station_new'),
    path('station/<int:pk>/edit', StationUpdateView.as_view(), name='station_edit'),
    path('station/<int:pk>/delete', views.station_delete, name='station_delete'),
    path('station/list/', StationListView.as_view(), name='station-list'),
    
    path('ship/new/', ShipCreateView.as_view(), name='ship_new'),
    path('ship/<int:pk>/edit', ShipUpdateView.as_view(), name='ship_edit'),
    path('ship/<int:pk>/delete', views.ship_delete, name='ship_delete'),
    path('ship/list/', ShipListView.as_view(), name='ship-list'),
    
    path('species/new/', SpeciesCreateView.as_view(), name='species_new'),
    path('species/<int:pk>/edit', SpeciesUpdateView.as_view(), name='species_edit'),
    path('species/<int:pk>/delete', views.species_delete, name='species_delete'),
    path('species/list/', SpeciesListView.as_view(), name='species-list'),
    path('ajax/load-genus/', views.load_genus, name='ajax_load_genus'),
    path('ajax/new-item/', views.new_item, name='ajax_new_item'),
    
    path('family/new/', FamilyCreateView.as_view(), name='family_new'),
    path('family/<int:pk>/edit', FamilyUpdateView.as_view(), name='family_edit'),
    path('family/<int:pk>/delete', views.family_delete, name='family_delete'),
    path('family/list/', FamilyListView.as_view(), name='family-list'),
    
    path('genus/new/', GenusCreateView.as_view(), name='genus_new'),
    path('genus/<int:pk>/edit', GenusUpdateView.as_view(), name='genus_edit'),
    path('genus/<int:pk>/delete', views.genus_delete, name='genus_delete'),
    path('genus/list/', GenusListView.as_view(), name='genus-list'),
    

    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view())
]
