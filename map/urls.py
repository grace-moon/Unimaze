from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ready', views.ready, name='ready'),
    path('3dmap/hrc/<int:pk>/', views.map_detail, {'building_num':0}, name='hrc_map_detail'),
    path('3dmap/mac_l/<int:pk>/', views.map_detail, {'building_num':18}, name='mac_l_map_detail'),
    path('3dmap/mac_m/<int:pk>/', views.map_detail, {'building_num':18}, name='mac_m_map_detail'),
    path('3dmap/ttd/<int:pk>/', views.map_detail, {'building_num':0}, name='ttd_map_detail'),
    path('3dmap/ep/<int:pk>/', views.map_detail, {'building_num':8}, name='ep_map_detail'),
    path('3dmap/ch/<int:pk>/', views.map_detail, {'building_num':1}, name='ch_map_detail'),
    path('3dmap/as/<int:pk>/', views.map_detail, {'building_num':2}, name='as_map_detail'),
    path('3dmap/sh/<int:pk>/', views.map_detail, {'building_num':3}, name='sh_map_detail'),
    path('3dmap/en/<int:pk>/', views.map_detail, {'building_num':4}, name='en_map_detail'),
    path('3dmap/hs/<int:pk>/', views.map_detail, {'building_num':6}, name='hs_map_detail'),
    path('3dmap/bs/<int:pk>/', views.map_detail, {'building_num':7}, name='bs_map_detail'),
    path('3dmap/jl/<int:pk>/', views.map_detail, {'building_num':10}, name='jl_map_detail'),
    path('3dmap/ee/<int:pk>/', views.map_detail, {'building_num':11}, name='ee_map_detail'),
    path('3dmap/om/<int:pk>/', views.map_detail, {'building_num':12}, name='om_map_detail'),
    path('3dmap/ad/<int:pk>/', views.map_detail, {'building_num':14}, name='ad_map_detail'),
    path('3dmap/hc/<int:pk>/', views.map_detail, {'building_num':15}, name='hc_map_detail'),
    path('3dmap/tsd/<int:pk>/', views.map_detail, {'building_num':16}, name='tsd_map_detail'),
    path('3dmap/mm/<int:pk>/', views.map_detail, {'building_num':19}, name='mm_map_detail'),
    path('3dmap/tta/<int:pk>/', views.map_detail, {'building_num':22}, name='tta_map_detail'),
    path('3dmap/tfd/<int:pk>/', views.map_detail, {'building_num':23}, name='tfd_map_detail'),
    path('3dmap/fs/<int:pk>/', views.map_detail, {'building_num':24}, name='fs_map_detail'),
    path('3dmap/iac/<int:pk>/', views.map_detail, {'building_num':25}, name='iac_map_detail'),
]