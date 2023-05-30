from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ready', views.ready, name='ready'),
    path('3dmap/hrc/<int:pk>/', views.map_detail, {'building_num':0}, name='map_detail'),
    path('3dmap/mac_l/<int:pk>/', views.map_detail, {'building_num':18}, name='map_detail'),
    path('3dmap/mac_m/<int:pk>/', views.map_detail, {'building_num':18}, name='map_detail'),
    path('3dmap/ttd/<int:pk>/', views.map_detail, {'building_num':0}, name='map_detail'),
    path('3dmap/ep/<int:pk>/', views.map_detail, {'building_num':8}, name='map_detail'),
    path('3dmap/ch/<int:pk>/', views.map_detail, {'building_num':1}, name='map_detail'),
    path('3dmap/as/<int:pk>/', views.map_detail, {'building_num':2}, name='map_detail'),
    path('3dmap/sh/<int:pk>/', views.map_detail, {'building_num':3}, name='map_detail'),
    path('3dmap/en/<int:pk>/', views.map_detail, {'building_num':4}, name='map_detail'),
    path('3dmap/hs/<int:pk>/', views.map_detail, {'building_num':6}, name='map_detail'),
    path('3dmap/bs/<int:pk>/', views.map_detail, {'building_num':7}, name='map_detail'),
    path('3dmap/jl/<int:pk>/', views.map_detail, {'building_num':10}, name='map_detail'),
    path('3dmap/ee/<int:pk>/', views.map_detail, {'building_num':11}, name='map_detail'),
    path('3dmap/om/<int:pk>/', views.map_detail, {'building_num':12}, name='map_detail'),
    path('3dmap/ad/<int:pk>/', views.map_detail, {'building_num':14}, name='map_detail'),
    path('3dmap/hc/<int:pk>/', views.map_detail, {'building_num':15}, name='map_detail'),
    path('3dmap/tsd/<int:pk>/', views.map_detail, {'building_num':16}, name='map_detail'),
    path('3dmap/mm/<int:pk>/', views.map_detail, {'building_num':19}, name='map_detail'),
    path('3dmap/tta/<int:pk>/', views.map_detail, {'building_num':22}, name='map_detail'),
    path('3dmap/tfd/<int:pk>/', views.map_detail, {'building_num':23}, name='map_detail'),
    path('3dmap/fs/<int:pk>/', views.map_detail, {'building_num':24}, name='map_detail'),
    path('3dmap/iac/<int:pk>/', views.map_detail, {'building_num': 25}, name='map_detail'),
]